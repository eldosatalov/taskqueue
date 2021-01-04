from django.urls import path
from task.views import TaskViewSet

task_list = TaskViewSet.as_view({
    'get': 'list',
})

task_create = TaskViewSet.as_view({
    'post': 'create',
})

task_detail = TaskViewSet.as_view({
    'put': 'start',
    'patch': 'partial_update',
})

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('create_task/', task_create, name='task_create'),
    path('task/<int:pk>/', task_detail, name='task_detail')
]

