from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)
    class Meta:
        model = Event
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
