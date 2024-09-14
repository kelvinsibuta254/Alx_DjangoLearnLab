# from django.urls import path
# from .views import register, profile #, index, 
# from django.contrib.auth.views import LoginView, LogoutView

# urlpatterns = [
#     #path("", index, name="index"),
#     path("register/", register, name="register"),
#     path("login/", LoginView.as_view(), name="login"),
#     path("profile/", profile, name="profile"),
#     path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
#     path('post/', List_view.as_view(), name='post_list'), 
#     path('post/<int:pk>/', Detail_View.as_view(), name='post_detail'),
#     path('post/new/', create_view.as_view(), name='post_create'), 
#     path('post/<int:pk>/update/', Update_View.as_view(), name='post_edit'),
#     path('post/<int:pk>/delete/', Delete_view.as_view(), name='post_delete'),
# ]

from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('posts/', views.posts.as_view(), name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.customlogin, name='login'),
    path('logout/', views.customlogout, name='logout'),
    path('post/new/', views.postcreate.as_view(), name='create-view'),
    path('posts/<int:pk>/',views.postdetail.as_view(), name='detail-view'),
    path('post/<int:pk>/update/', views.postupdate.as_view(), name='update-view'),
    path('post/<int:pk>/delete/', views.postdelete.as_view(), name='delete-view'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create-view'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update-view'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete-view'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view()),
    path('search/', views.SearchResultView.as_view()),
]