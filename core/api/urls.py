from django.urls import path
from api.views import ProjectDeleteView, ProjectUpdateView, ProjectDetailView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('project/detail/<int:pk>', ProjectDetailView.as_view(), name='detail-project'),
    path('project/update/<int:pk>', ProjectUpdateView.as_view(), name='update-project'),
    path('project/delete/<int:pk>', ProjectDeleteView.as_view(), name='delete-project'),
    path('project/task/detail/<int:pk>', TaskDetailView.as_view(), name='detail-task'),
    path('project/task/update/<int:pk>', TaskUpdateView.as_view(), name='update-task'),
    path('project/task/delete/<int:pk>', TaskDeleteView.as_view(), name='delete-task')
]
