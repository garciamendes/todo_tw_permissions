# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Third party
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.models import ActivatorModel
from django_extensions.db.models import TitleDescriptionModel


def validator_relevant(value):
    if 0 > value > 3:
        raise ValidationError('Invalid value Relevant')


class Task(TimeStampedModel, ActivatorModel, TitleDescriptionModel):
    user = models.ForeignKey(
        get_user_model(),
        related_name='tasks',
        on_delete=models.CASCADE)

    is_finished = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'


class CommentTask(TimeStampedModel, ActivatorModel):
    comment = models.TextField(max_length=150, null=True, blank=True)

    task = models.ForeignKey(
        Task,
        related_name='comments',
        on_delete=models.CASCADE)

    relevant = models.IntegerField(
        default=0,
        validators=[validator_relevant])

    def __str__(self) -> str:
        return f'{self.id} - {self.relevant}'
