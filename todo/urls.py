# Third party
from django.urls import path
from django.urls import include
from rest_framework.routers import SimpleRouter

# Local
from .views import TaskViewset
from .views import CommentTaskViewset

router = SimpleRouter()

router.register(r'task', TaskViewset, basename='task')
router.register(r'(?P<task_id>\d+)/comment', CommentTaskViewset, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
