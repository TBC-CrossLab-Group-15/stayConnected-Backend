from django.urls import path
from . import views
from .views import RegisterView, LoginView, RefreshTokenCustomView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", RefreshTokenCustomView.as_view(), name="token_refresh"),
    path("leaderboard/",UserListView.as_view(), name='leaderboard')
]