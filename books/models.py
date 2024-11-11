from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
    )
    
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    
    rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00
    )
    
    description = models.TextField(
        blank=True,
        null=True
    )
    
    published = models.DateField(
        blank=True,
        null=True
    )
    

    # foreign key for author_id field in Author model, category_id field in Category model
    

    def __str__(self) :
        return self.title
        
    