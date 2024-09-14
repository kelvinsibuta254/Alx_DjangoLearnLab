from django.urls import path
from .views import index, register, LoginView, product
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile", product, name="profile"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout")
]