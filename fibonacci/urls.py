from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from .views import get_fibonacci
router = SimpleRouter()

urlpatterns = [
    url('', include(router.urls)),
    url(r'^fibonacci/', get_fibonacci),
]