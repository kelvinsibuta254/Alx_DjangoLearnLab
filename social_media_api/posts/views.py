from django.shortcuts import render
from rest_framework import filters, generics, viewsets
from .serializers import CommentSerializer, PostSerializer
from django.conf import settings
from .models import Post, Comment
from rest_framework import permissions
from rest_framework.views import APIView
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

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'message': 'You have already liked this post'}, status = status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=user, post=post)

        if post.author != user:
            Notification.objects.create(
                recipient = post.author,
                actor = user,
                verb = 'liked',
                target = post
            )

            return Response({'message':'Congratulatios! Kelvin liked your post'}, status=status.HTTP_200_OK)


class UnlikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if like:
            like.delete()
            return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have not liked this post yet!!'}, status=status.HTTP_400_BAD_REQUEST)  


        
        