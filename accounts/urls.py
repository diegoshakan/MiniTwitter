from django.urls import path, include
from rest_framework import routers
from. views import MyUserModelViewSet

router = routers.DefaultRouter()
router.register('myuser', MyUserModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]