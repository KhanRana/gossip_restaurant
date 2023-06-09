from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Menu(models.Model):
    """Create menu model"""
    title = models.CharField(max_length=50, unique=True)
    content = models.CharField(max_length=300)
    price = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='menu_likes', blank=True)

    def __str__(self):
        return self.title

    def num_of_Likes(self):
        return self.likes.count()


class Table(models.Model):
    """Creates table model"""
    accommodate = (
        (1, 1),
        (2, 2),
        (4, 4),
        (6, 6),
    )
    num = models.PositiveIntegerField()
    capacity = models.IntegerField(choices=accommodate)

    def __str__(self):
        return f'{self.capacity}'


TIME_CHOICES = (
    ('6 PM', '6 PM'),
    ('7 PM', '7 PM'),
    ('8 PM', '8 PM'),
    ('9 PM', '9 PM'),
)


class Booking(models.Model):
    """Creates booking model to book a table"""
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='table')
    date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)])
    time = models.CharField(choices=TIME_CHOICES)

    def __str__(self):
        return f'''Table for {self.table}, and has been booked for {self.date}
        {self.time}'''


class Review(models.Model):
    """Create review model"""
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Review {self.body} by {self.name}'
