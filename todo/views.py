# Third party
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Local
from .models import Task
from .models import CommentTask
from .serializers import TasksSerializer
from .serializers import CommentTasksSerializer
from todo.mixins import TaskMixin


class TaskViewset(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['title']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CommentTaskViewset(TaskMixin, ModelViewSet):
    queryset = CommentTask.objects.all()
    serializer_class = CommentTasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CommentTask.objects.filter(task=self.task)
