# Generated by Django 5.1.3 on 2024-11-12 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_email'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='customUser',
            new_name='User',
        ),
    ]
