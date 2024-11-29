from rest_framework import serializers

from posts.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','text','tags','user']