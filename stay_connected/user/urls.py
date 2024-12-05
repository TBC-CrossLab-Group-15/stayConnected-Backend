from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterView, LoginView, RefreshTokenCustomView, UserListView, RetrieveUser, AvatarListing, \
    UserInfoView, LogoutView, CurrentUserQuestions

router = DefaultRouter()

router.register('profile', RetrieveUser, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", RefreshTokenCustomView.as_view(), name="token_refresh"),
    path("leaderboard/", UserListView.as_view(), name='leaderboard'),
    path("avatars/", AvatarListing.as_view(), name='avatars'),
    path("currentuser/", UserInfoView.as_view(), name='currentuser'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('currentuserquestions/',CurrentUserQuestions.as_view(), name="currentuserquestions")
]
