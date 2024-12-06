from django.contrib import admin
from posts.models import Question, Tag, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "user",
        "create_date"
    )
    search_fields = (
        "title",
        "text"
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "question",
        "isCorrect",
        "user",
        "create_date"
    )
    search_fields = (
        "text",
        "question"
    )
