from django.urls import path

from .views import UserRegisterView, LoginView, LogoutView, ProfileUpdateView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile', ProfileUpdateView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('follow/<int:user_id>/', FollowUserView.as_view()),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view()),

]