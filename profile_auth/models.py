# Django
from django.db import models
from django.contrib.auth import get_user_model

# Third party
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.models import ActivatorModel


class Profile(TimeStampedModel, ActivatorModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
