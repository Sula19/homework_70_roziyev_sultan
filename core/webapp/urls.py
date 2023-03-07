from django.urls import path
from webapp.views.template_views import IndexViews, DetailView, UpdateView, CreateView, DeleteView

urlpatterns = [
    path('', IndexViews.as_view(), name='home'),
    path('tasks/detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('tasks/update/<int:pk>', UpdateView.as_view(), name='update'),
    path('tasks/create', CreateView.as_view(), name='create'),
    path('tasks/delete/<int:pk>', DeleteView.as_view(), name='delete')
]