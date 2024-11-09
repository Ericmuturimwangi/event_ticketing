from django.db import models
from django.contrib.auth.models import User

class Event (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.title
    
class Ticket (models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.event.title}"
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField (max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    
    
    
    
