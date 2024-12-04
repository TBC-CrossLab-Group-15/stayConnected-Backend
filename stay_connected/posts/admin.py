from django.contrib import admin
from posts.models import Question, Tag, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
