from .views import BookListAPIView, BookViewset
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    ]

router = DefaultRouter()
router.register('api/', BookViewset, basename='api')
urlpatterns = router.urls