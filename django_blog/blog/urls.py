from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from blog import views
from .views import register, customlogout, home, profile, postdetail, Edit, postcreate, postupdate, postdelete, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView, SearchResultView

urlpatterns=[
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('posts/', views.Post.as_view(), name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('edit/', views.Edit, name='edit'),
    path('new/', views.postcreate.as_view(), name='create-view'),
    path('posts/<int:pk>/', views.postdetail.as_view(), name='detail-view'),
    path('post/<int:pk>/update/', views.postupdate.as_view(), name='update-view'),
    path('post/<int:pk>/delete/', views.postdelete.as_view(), name='delete-view'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create-view'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update-view'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete-view'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view()),
    path('search/', views.SearchResultView.as_view()),
]