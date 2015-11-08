from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

battle_classes = (
    ('Water', 'Water'),
    ('Fire', 'Fire'),
    ('Wind', 'Wind'),
    ('Earth', 'Earth'),
    ('Light', 'Light'),
    ('Dark', 'Dark')
)

class Image(models.Model):
    image_desc = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date uploaded')
    image = models.ImageField(upload_to='images')
    wins = models.IntegerField()
    loses = models.IntegerField()

    def __str__(self):
        return self.image_desc

    def is_recent(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    is_recent.admin_order_field = 'pub_date'
    is_recent.boolean = True
    is_recent.short_description = "Published in the last day?"

    def is_hot(self):
        return self.wins / (self.loses + 1) >= 1.0 and self.wins >= 50
    is_hot.admin_order_field = 'wins'
    is_hot.boolean = True
    is_hot.short_description = "Hot Image?"


class Card(models.Model):
    """
        Add XP/Levels? Allow leveling up cards for better strength?
        Allow combination of cards and max out at certain level?
        e.g. take atk of one and add it to another and add levels together?

    """


    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    klass = models.CharField(max_length=10, choices=battle_classes)
    image = models.OneToOneField(Image, max_length=10)
    health = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    fire = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    earth = models.IntegerField(default=0)
    light = models.IntegerField(default=0)
    dark = models.IntegerField(default=0)

    def __str__(self):
        return self.name
