from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

        def create(self, validated_data):
            likes_info = validated_data.pop('likes')
            notification = Notification.objects.create(**validated_data)
            for like_info in likes_info:
                Notification.objects.create(like=like, **like_info)
            return like
