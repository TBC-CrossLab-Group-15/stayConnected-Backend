from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import CreateQuestionViewset, TagListing, AnswerViewSet
from posts.views import QuestionList

router = DefaultRouter()
router.register(r'questions', CreateQuestionViewset)
router.register('answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tags/', TagListing.as_view(), name='tags'),
    path('search/',QuestionList.as_view(),name='search')
]
