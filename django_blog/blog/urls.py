from django.urls import path
from .views import index, register, LoginView, product
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name="index"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", product, name="profile"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path('post/', List_view.as_view(), name='post_list'), 
    path('post/<int:pk>/', Detail_View.as_view(), name='post_detail'),
    path('post/new/', create_view.as_view(), name='post_create'), 
    path('post/<int:pk>/update/', Update_View.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', Delete_view.as_view(), name='post_delete'),
]