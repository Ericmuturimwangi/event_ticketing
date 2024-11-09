from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from ticketing.models import Order
from ticketing.serializers import OrderSerializer
from ticketing.models import Ticket, Event
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class BuyTicketView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ticket_id = self.request.data['ticket']
        event_id = self.request.data['event']

        try:
            ticket = Ticket.objects.get(id=ticket_id, event=event_id)
        except Ticket.DoesNotExist:
            return Response({"error":"Ticket not found for the event"}, status=status.HTTP_400_BAD_REQUEST)
        

        # calculating the total price

        quantity = self.request.data['quantity']
        total_price = ticket.price * quantity

        # saving the order
        serializer.save(user=self.request.user, ticket=ticket, total_price=total_price, status="pending")

class OrderListView(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer =OrderSerializer(orders, many=True)
        return Response(serializer.data)