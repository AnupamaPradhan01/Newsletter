# newsletter/views.py
from rest_framework import viewsets

from .models import Newsletter, Subscriber
from .serializers import NewsletterSerializer, SubscriberSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
