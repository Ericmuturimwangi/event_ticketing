from rest_framework import serializers
from .models import Order
from ticketing.models import Ticket, Event

class OrderSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['ticket', 'event', 'quantity', 'total_price', 'user', 'status']

    def validate(self, data):
        ticket = data.get('ticket')
        quantity = data.get('quantity')

        if ticket.available_quantity < quantity:
            raise serializers.ValidationError("Not ENough tickets available.")