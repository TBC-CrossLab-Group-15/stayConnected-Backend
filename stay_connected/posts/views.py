from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from posts.serializers import QuestionSerializer
from rest_framework.decorators import action
from posts.models import Question
from rest_framework.response import Response


# Create your views here.
@extend_schema(tags=['postebi'])
class CreateQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    @action(detail=False, methods=['post'])
    def create_question(self,request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save(user=request.user)
            return Response({"question": QuestionSerializer(question).data})
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()

        if question.user != request.user:
            return Response(
                {"error": "You do not have permission to delete this question."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().destroy(request, *args, **kwargs)



