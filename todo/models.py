# Django
from django.db import models
from django.contrib.auth import get_user_model

# Third party
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.models import ActivatorModel
from django_extensions.db.models import TitleDescriptionModel


class Todo(TimeStampedModel, ActivatorModel, TitleDescriptionModel):
    user = models.ForeignKey(
        get_user_model(),
        related_name='todos',
        on_delete=models.CASCADE)

    is_finished = models.BooleanField(default=False, blank=True, null=True)
