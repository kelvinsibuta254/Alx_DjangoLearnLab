# from django.db import models
# from django.conf import settings
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# # Create your models here.
# class Notification(models.Model):
#     recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notification_receiver')
#     actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notification_sender')
#     verb = [
#         ('Follow', 'notification on new following'),
#         ('Post', 'notification on new post'),
#         ('Like', 'notification on new post like'),
#         ('Comment', 'notification on post comments'),
#     ]
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     target = GenericForeignKey('content_type', 'object_id')
#     timestamp = models.DateField(auto_now=True)


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor')
    verb = models.CharField(max_length=100)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Notification to {self.recipient} from {self.actor}: {self.verb}"