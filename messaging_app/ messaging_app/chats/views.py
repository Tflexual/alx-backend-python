from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MessageViewSet(viewsets.ModelViewSet):
    ...
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MessageFilter
