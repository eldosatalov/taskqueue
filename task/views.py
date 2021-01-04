import datetime

from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from task.models import Task
from task.serializers import TaskSerializer, TaskCreateSerializer


class TaskViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        if self.action == 'list':
            return Task.objects.filter(success__isnull=True)
        return Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TaskCreateSerializer
        return TaskSerializer

    @action(detail=True)
    def start(self, request, *args, **kwargs):
        task = self.get_object()
        task.start_date = datetime.datetime.now()
        task.save()
        output_serializer = TaskSerializer(task)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_200_OK, headers=headers)
