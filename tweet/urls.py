from django.urls import path, include
from rest_framework import routers
from .views import TweetModelViewSet
from django.views.generic import TemplateView
from .models import Tweet

router = routers.DefaultRouter()
router.register('', TweetModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('index/todos', TemplateView.as_view(template_name='tweet/index.html'), {'tweets': Tweet.objects.all()}),
]