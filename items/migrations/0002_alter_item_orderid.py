# Generated by Django 5.1.3 on 2024-11-12 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('orders', '0002_order_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
