from django.db import models
from django.db.models import Model
from user.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.TextField(null=False, verbose_name=_("Title"))
    text = models.TextField(null=True, verbose_name=_("Text"))
    tags = models.ManyToManyField(Tag, related_name="questions", verbose_name=_("Tags"))
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name=_("Author"))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Create date"))

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField(null=False, verbose_name=_("Text"))
    isCorrect = models.BooleanField(default=False, verbose_name=_("Correct"))
    likes = models.IntegerField(default=0, verbose_name=_("Likes"))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Create date"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers", verbose_name=_("User"))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", verbose_name=_("Question"))

    def __str__(self):
        return self.text[:25]

