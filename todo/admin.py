# Django
from django.contrib import admin

# Local
from .models import Task
from .models import CommentTask


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_finished']


class CommentsTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task']


admin.site.register(Task, TaskAdmin)
admin.site.register(CommentTask, CommentsTaskAdmin)
