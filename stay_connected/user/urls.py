from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterView, LoginView, RefreshTokenCustomView, UserListView, RetrieveUser

router = DefaultRouter()

router.register('profile', RetrieveUser, basename='profile')

urlpatterns = [
    path('profile/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", RefreshTokenCustomView.as_view(), name="token_refresh"),
    path("leaderboard/",UserListView.as_view(), name='leaderboard')
]