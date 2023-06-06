# Generated by Django 4.2.1 on 2023-06-06 16:51

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_menu_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today)]),
        ),
    ]
