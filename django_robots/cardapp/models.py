from django.db import models
from django.contrib.auth.models import User

# Create your models here.

battle_classes = (
    ('Water', 'Water'),
    ('Fire', 'Fire'),
    ('Wind', 'Wind'),
    ('Earth', 'Earth'),
    ('Light', 'Light'),
    ('Dark', 'Dark')
)

class Card(models.Model):
    card_name = models.CharField(max_length=200)
    card_desc = models.CharField(max_length=1000)
    img = models.CharField(max_length=200)
    health = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    fire = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    earth = models.IntegerField(default=0)
    light = models.IntegerField(default=0)
    dark = models.IntegerField(default=0)
    klass = models.CharField(max_length=10, choices=battle_classes)

    def __str__(self):
        return str(self.pk) + '. ' + self.card_name

class Deck(models.Model):
    title = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)
    # owner = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def count(self):
        return self.cards.count()
