# newsletter/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NewsletterViewSet, SubscriberViewSet

router = DefaultRouter()
router.register(r"subscribers", SubscriberViewSet)
router.register(r"newsletters", NewsletterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
