from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.CharField(source='recipient.username', read_only=True)
    actor = serializers.CharField(source='actor.username', read_only=True)
    target = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields = '__all__'

        def get_target(self, validated_data):
            likes_info = validated_data.pop('likes')
            notification = Notification.objects.create(**validated_data)
            for like_info in likes_info:
                Notification.objects.create(like=like, **like_info)
            return like
