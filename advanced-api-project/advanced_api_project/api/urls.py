
from rest_framework.routers import DefaultRouter
from .views import BookViewset


router = DefaultRouter()
"""router returns a list of urlpatterns"""

router.register("api", BookViewset, basename="api")

urlpatterns = router.urls