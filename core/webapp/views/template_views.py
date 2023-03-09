from django.utils.http import urlencode
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from webapp.forms import TasksForm, ProjectForm, SearchView
from webapp.models import Tasks, Project
from django.shortcuts import get_object_or_404, redirect, reverse
from django.db.models import Q


class DeleteProject(DeleteView):
    template_name = 'delete_project.html'
    context_object_name = 'project'
    model = Project
    success_url = '/'


class CreateProject(CreateView):
    template_name = 'create_project.html'
    model = Project
    form_class = ProjectForm
    success_url = '/'


class DetailProject(DetailView):
    template_name = 'detail_project.html'
    model = Project


class IndexProjects(ListView):
    template_name = 'home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.exclude(is_deleted=True)


class IndexViews(ListView):
    template_name = 'index_tasks.html'
    context_object_name = 'tasks'
    model = Tasks
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchView(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class CreateTask(CreateView):
    template_name = 'create_task.html'
    model = Tasks
    form_class = TasksForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('/')


class DetailView(TemplateView):
    template_name = 'detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context


class UpdateViews(UpdateView):
    template_name = 'update_task.html'
    model = Tasks
    form_class = TasksForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})


class DeleteViews(DeleteView):
    template_name = 'delete_task.html'
    model = Tasks
    context_object_name = 'task'
    success_url = '/'
