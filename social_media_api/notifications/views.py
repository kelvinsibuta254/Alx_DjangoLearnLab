from django.shortcuts import render
from rest_framework import generics
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        unread = Notification.objects.filter(recipient=user, is_read=False)
        read = Notification.objects.filter(recipient=user, is_read=True)
        return unread | read