# Third party
from rest_framework import serializers

# Local
from .models import Task
from .models import CommentTask


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_finished', 'created', 'modified']


class CommentTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTask
        fields = ['id', 'comment', 'task', 'relevant', 'created', 'modified']
