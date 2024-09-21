from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer
# Create your views here.

class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'user': serializer.data,
                'token': Token.objects.get(user=User.objects.get(username=serializer.data['username'])).key()
            }

            return Response(response, status=status.HTTP_200_OK)
        raise ValidationError(serializer.errors, code=status.HTTP_406_NOT_ACCEPTABLE)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {'username': {'detail': 'User does not exist!', }, }
            userdata = User.objects.filter(username=request.data['username'])
            if userdata.exists():
                user = User.objects.get(username=request.data['username'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                    'token': token.key
                }

                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'success': True, 'detail': "Logged out Successfully"}, status=status.HTTP_200_OK)

class ProfileUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        serializer.save()


User = get_user_model()

class FollowUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_to_follow = get_object_or_404(User, id=self.kwargs['user_id'])
        if not user.following.filter(id=user_to_follow.id).exist():
            user.following.add(user_to_follow)
            return Response({'message': 'Followed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You already followed this user'}, status=status.HTTP_400_BAD_REQUEST)


class UnfollowUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user=self.request.user
        user_to_unfollow = get_object_or_404(User, id=self.kwargs['user_id'])
        if user.following.filter(id=user_to_unfollow.id).exists():
            user.following.remove(user_to_unfollow)
            return Response({'message': 'Unfollowed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You nolonger follow this user!'}, status=status.HTTP_400_BAD_REQUEST)