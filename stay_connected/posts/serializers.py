from rest_framework import serializers
from posts.models import Question, Tag, Answer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'text', 'tags', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
            # Automatically set the user from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)


class CreateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'question']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'