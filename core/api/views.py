from rest_framework.views import APIView
from rest_framework.response import Response
from webapp.models import Project, Tasks
from .serializers import ProjectSerializer, TaskSerializer
from django.core.exceptions import ObjectDoesNotExist


class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            project = Project.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})
        serialize = ProjectSerializer(project)
        return Response(serialize.data)


class TaskDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            task = Tasks.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})
        serialize = TaskSerializer(task)
        return Response(serialize.data)


class ProjectUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            project = Project.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})
        serialize = ProjectSerializer(data=request.data, instance=project)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
        return Response(serialize.data)


class TaskUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            task = Tasks.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})
        serialize = TaskSerializer(data=request.data, instance=task)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
        return Response(serialize.data)


class ProjectDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            project = Project.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})
        project.delete()
        return Response({'delete': f'Delete post {pk}'})


class TaskDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            task = Tasks.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})
        task.delete()
        return Response({'delete': f'Delete task {pk}'})
