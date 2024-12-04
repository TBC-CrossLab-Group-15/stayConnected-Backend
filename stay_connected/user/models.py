from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class Avatar(models.Model):
    id = None
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField(default=0, verbose_name=_("Rating"))
    my_answers = models.IntegerField(default=0, verbose_name=_("Answers"))
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='users', null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
