from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    rating = models.IntegerField(default=0, verbose_name=_("Rating"))
    correct_answers = models.IntegerField(default=0, verbose_name=_("Correct Answers"))
    # profile_picture = models.ImageField(upload_to='profile_pictures')

    def __str__(self):
        return self.username
