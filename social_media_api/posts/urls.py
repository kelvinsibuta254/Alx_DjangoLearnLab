from rest_framework import routers
from django.urls import path, include
from .views import CreatePost, ListPost, UpdatePost, DeletePost, PostFeed, CreateComment, ListComment, UpdateComment, DeleteComment


router = routers.DefaultRouter()
router.register('Post', ListPost, basename='post')
urlpatterns = [
    path('post/new', CreatePost.as_view() ),
    path('post/list', ListPost.as_view({'get': 'list'})),
    path('post/<int:pk>/update/', UpdatePost.as_view()),
    path('post/<int:pk>/delete', DeletePost.as_view()),
    path('post/<int:pk>/comment/new/', CreateComment.as_view()),
    path('comment/list', ListComment.as_view()),
    path('comment/<int:pk>/update/', UpdateComment.as_view()),
    path('comment/<int:pk>/delete', DeleteComment.as_view()),
    path('feed/', PostFeed.as_view()),
]