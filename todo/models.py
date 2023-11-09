# Django
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

# Third party
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.models import ActivatorModel
from django_extensions.db.models import TitleDescriptionModel


class Task(TimeStampedModel, ActivatorModel, TitleDescriptionModel):
    user = models.ForeignKey(
        get_user_model(),
        related_name='tasks',
        on_delete=models.CASCADE)

    is_finished = models.BooleanField(default=False, blank=True, null=True)


class CommentTask(TimeStampedModel, ActivatorModel):
    comment = models.TextField(max_length=150, null=True, blank=True)

    task = models.ForeignKey(
        Task,
        related_name='tasks',
        on_delete=models.CASCADE)

    relevant = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(3)])
