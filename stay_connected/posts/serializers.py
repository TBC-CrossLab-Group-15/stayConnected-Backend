from rest_framework import serializers
from user.serializers import UserStatSerializer
from posts.models import Question, Tag, Answer, Like


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CreateQuestionSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all().filter()
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'text', 'tags', 'user']

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

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'like_status']
        read_only_fields = ['answer']

class AnswerSerializer(serializers.ModelSerializer):
    user = UserStatSerializer()
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'text', 'isCorrect', 'user', 'question', 'create_date', 'likes','likes_count']

    def get_likes_count(self, obj):
        # Count the number of likes for this answer
        return Like.objects.filter(answer=obj, like_status=1).count()

class UpdateAnswerSerializer(serializers.ModelSerializer):
    isCorrect = serializers.BooleanField(default=False)
    class Meta:
        model = Answer
        fields = ['isCorrect']

class ListQuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    answers = AnswerSerializer(many=True)
    user = UserStatSerializer()

    class Meta:
        model = Question
        fields = "__all__"
