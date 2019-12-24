from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import get_ackermann
router = SimpleRouter()

urlpatterns = [
    url('', include(router.urls)),
    url(r'^ackermann/', get_ackermann),
]