from django.views.generic import TemplateView
from webapp.forms import TasksForm
from webapp.models import Tasks
from django.shortcuts import get_object_or_404, redirect, render


class IndexViews(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()
        return context


class CreateView(TemplateView):
    template_name = 'create_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TasksForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create_task.html', context={'form': form})


class DetailView(TemplateView):
    template_name = 'detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context


class UpdateView(TemplateView):
    template_name = 'update_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        context['form'] = TasksForm(instance=context['task'])
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs['pk'])
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'update_task.html', context={'form': form, 'task': task})


class DeleteView(TemplateView):
    template_name = 'delete_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context

    def post(self, *args, **kwargs):
        task = get_object_or_404(Tasks, pk=kwargs['pk'])
        task.delete()
        return redirect('home')