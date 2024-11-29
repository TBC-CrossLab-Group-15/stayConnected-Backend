from django.urls import path,include
from rest_framework.routers import DefaultRouter

from posts.views import CreateQuestionViewset

router = DefaultRouter()
router.register(r'/questions', CreateQuestionViewset)

urlpatterns = [
    path('', include(router.urls)),


]
