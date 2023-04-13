from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    class Meta:
        db_table = 'user'

    user_chg = models.DateTimeField(auto_now=True)
    nickname = models.CharField(max_length=20, default='')