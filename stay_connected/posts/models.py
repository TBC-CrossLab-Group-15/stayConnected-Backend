from django.db import models
from django.db.models import Model
from user.models import User


# Create your models here.
class Question(models.Model):
    text = models.TextField(null=False)
    tags = models.CharField(max_length=150,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


