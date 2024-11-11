from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class customUser(models.Model):
    username = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )
    
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    
    password = models.CharField(
        max_length=18,
        null=False,
        blank=False,
    )
    
    address = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    
    phoneNumber = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        validators=[
            RegexValidator(
                regex='^0[0-9]{10}$',
                message='Phone number must be 11 digits and start with 0',
                code='invalid_phone_number'
            )
        ]
    )
    
    def __str__(self):
        return self.username
    
    