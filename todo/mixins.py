# Third party
from rest_framework.generics import get_object_or_404

# Local
from .models import Task


class TaskMixin:
    def dispatch(self, request, *args, **kwargs):
        task_id = kwargs.pop('task_id', None)
        self.task = get_object_or_404(Task, id=task_id)
        return super().dispatch(request, *args, **kwargs)
