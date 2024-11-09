from django.db import models
from ticketing.models import Ticket
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_orders')
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='purchase_tickets_orders')
    event = models.ForeignKey('ticketing.Event', on_delete=models.CASCADE, related_name='purchase_event_orders')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Order by {self.user.username} for {self.ticket.name}"
    
