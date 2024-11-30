from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status, generics, filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from posts.serializers import TagSerializer, CreateAnswerSerializer, AnswerSerializer, \
    CreateQuestionSerializer, ListQuestionSerializer
from rest_framework.decorators import action, permission_classes
from posts.models import Question, Tag, Answer
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializer_utils import SerializerFactory

# Create your views here.
@extend_schema(tags=['Postebi'])
class CreateQuestionViewset(viewsets.ModelViewSet):
    serializer_class = SerializerFactory(
        create=CreateQuestionSerializer,
        list=ListQuestionSerializer,
        default=ListQuestionSerializer
    )
    queryset = Question.objects.select_related('user').prefetch_related('tags')

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=request.user)


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


@extend_schema(tags=["Searchi"])
class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = ListQuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__name']
    permission_classes = [AllowAny]
