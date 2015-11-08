from django.contrib import admin
from .models import Image, Card

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image', {'fields': ['image']}),
        ('Image Information', {'fields': [
            'image_desc',
            'wins',
            'loses',
        ]}),
        ('Time Stamp', {'fields': ['pub_date']})
    ]

    list_display = ('image_desc', 'wins', 'loses', 'is_hot', 'is_recent', 'image')

    list_filter = ['pub_date']
    search_fields = ['image_desc']

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Quick Look', {'fields': ['image', 'name']}),
        ('Battle Stats', {'fields': [
            'fire',
            'water',
            'earth',
            'wind',
            'dark',
            'light',
            'health',
        ]}),
        ('Description', {'fields': ['klass', 'desc']})
    ]

    list_display = ('name', 'klass', 'image')

    list_filter = ['klass']
    search_fields = ['name']



admin.site.register(Image, ImageAdmin)
admin.site.register(Card, CardAdmin)
