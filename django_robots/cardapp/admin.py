from django.contrib import admin
from .models import *

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Quick Look', {'fields': ['img', 'card_name']}),
        ('Battle Stats', {'fields': [
            'fire',
            'water',
            'earth',
            'wind',
            'dark',
            'light',
            'health',
        ]}),
        ('Description', {'fields': ['klass', 'card_desc']})
    ]

    list_display = ('card_name', 'klass', 'img')

    list_filter = ['klass']
    search_fields = ['card_name']

class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'count')
    search_fields = ['title']

admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)
