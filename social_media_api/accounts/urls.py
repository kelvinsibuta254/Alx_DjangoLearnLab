from django.urls import path

from .views import UserRegisterView, LoginView, LogoutView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile', ProfileUpdateView.as_view()),
    path('logout/', LogoutView.as_view()),
]