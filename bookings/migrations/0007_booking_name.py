# Generated by Django 4.2.1 on 2023-05-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_rename_name_booking_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='admin', max_length=20),
        ),
    ]
