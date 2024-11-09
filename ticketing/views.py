from django.shortcuts import render
from ticketing.serializers import EventSerializer, TicketSerializer, OrderSerializer
from .models import Event, Ticket, Order
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ListEventViews(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class= EventSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
