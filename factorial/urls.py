from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import get_factorial
router = SimpleRouter()

urlpatterns = [
    url('', include(router.urls)),
    url(r'^factorial/', get_factorial),
]