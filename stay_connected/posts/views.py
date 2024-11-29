from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from posts.serializers import QuestionSerializer, TagSerializer, CreateAnswerSerializer, AnswerSerializer
from rest_framework.decorators import action, permission_classes
from posts.models import Question, Tag, Answer
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializer_utils import SerializerFactory

# Create your views here.
@extend_schema(tags=['postebi'])
class CreateQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['post'])
    def create_question(self,request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save(user=request.user)
            return Response({"question": QuestionSerializer(question).data})
        else:
            return Response(serializer.errors, status=400)


@extend_schema(tags=["Tagebi"])
class TagListing(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["Pasuxebi"])
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.select_related('user', 'question')
    serializer_class = SerializerFactory(
        create=CreateAnswerSerializer,
        default=AnswerSerializer
    )

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

