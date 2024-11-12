from django.db import models

# Create your models here.
class Order(models.Model):
    PENDING = 'pending'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (CANCELED, 'Canceled'),
    ]
    
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default=PENDING,
        null=False,
        blank=False,
    )
    
    totalPrice = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    
    orderDate = models.DateTimeField(
        auto_now_add=True,
    )
    
     # foreign key for the customer_id field
    
    def __str__(self):
        return f'Order #{self.id}'