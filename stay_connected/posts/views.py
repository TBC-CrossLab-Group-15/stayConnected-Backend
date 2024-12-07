from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status, generics, filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from posts.serializers import TagSerializer, CreateAnswerSerializer, AnswerSerializer, \
    CreateQuestionSerializer, ListQuestionSerializer, UpdateAnswerSerializer
from rest_framework.decorators import action, permission_classes
from posts.models import Question, Tag, Answer
from rest_framework.response import Response
from .pagination import CustomPageNumberPagination
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
    queryset = Question.objects.select_related('user').prefetch_related('tags').order_by("-create_date")
    pagination_class = CustomPageNumberPagination

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
        update=UpdateAnswerSerializer,
        partial_update=UpdateAnswerSerializer,
        default=AnswerSerializer
    )

    def get_permissions(self):
        if self.action == 'update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        self.request.user.my_answers += 1
        self.request.user.save()

    def update(self, request, *args, **kwargs):
        answer = self.get_object()
        if answer.question.user != request.user:
            return Response(
                {"detail": "You don't have permission to update this answer."},
                status=status.HTTP_403_FORBIDDEN
            )
        if 'isCorrect' in request.data and request.data['isCorrect'] == True and answer.isCorrect == False:
            answer.isCorrect = True
            answer.user.rating += 1
            answer.save()
            answer.user.save()
        elif answer.isCorrect and request.data['isCorrect'] == False:
            answer.isCorrect = False
            if answer.user.rating>0:
                answer.user.rating -= 1
            answer.save()
            answer.user.save()

        serializer = self.get_serializer(answer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@extend_schema(tags=["Searchi"])
class QuestionList(generics.ListAPIView):
    queryset = Question.objects.select_related('user').prefetch_related('tags').order_by('-create_date')
    serializer_class = ListQuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=tags__name']
    permission_classes = [AllowAny]


@extend_schema(tags=["Searchi"])
class QuestionTextList(generics.ListAPIView):
    queryset = Question.objects.select_related('user').prefetch_related('tags').order_by('-create_date')
    serializer_class = ListQuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'title']
    permission_classes = [AllowAny]
