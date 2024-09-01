from .views import BookListAPIView, BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('api/', include('api.urls'))
    ]

router = DefaultRouter()
router.register('api/', BookViewSet, basename='api')
urlpatterns = router.urls