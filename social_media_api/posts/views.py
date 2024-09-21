from django.shortcuts import render
from rest_framework import filters, generics, viewsets
from .serializers import CommentSerializer, PostSerializer
from django.conf import settings
from .models import Post, Comment
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        author = get_object_or_404(settings.AUTH_USER_MODEL, id=self.request.data.get('author'))
        return serializer.save(author=author)

class ListPost(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class UpdatePost(generics.RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

class DeletePost(generics.RetrieveDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

class PostFeed(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = self.request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('created_at')
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# For Comment model
class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        author = get_object_or_404(settings.AUTH_USER_MODEL, id=self.request.data.get('author'))
        return serializer.save(author=author)

class ListComment(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = LimitOffsetPagination

class UpdateComment(generics.RetrieveUpdateAPIView):
    serializer_class = CommentSerializer
    queryset  = Comment.objects.all()
    permission_classes = [IsAuthenticated]

class DeleteComment(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
