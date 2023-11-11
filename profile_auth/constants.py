# Django
from django.db import models


class UserRoles(models.IntegerChoices):
    USER_MODER = 1, 'usuário moderador'
    USER_MASTER = 2, 'usuário master'
    USER_NORMAL = 3, 'usuário normal'
