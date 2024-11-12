from django.db import models

# Create your models here.

class Item(models.Model):
    quantity = models.IntegerField(
        null=False,
        default=1,
    )
    
    totalPrice = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    
    orderId = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
    )
    
    bookId = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f'Item #{self.id}'
    