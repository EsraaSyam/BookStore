# Generated by Django 5.1.3 on 2024-11-11 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=18, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be 11 digits and start with 0', regex='^0[0-9]{11}$')])),
            ],
        ),
    ]
