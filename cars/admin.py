from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:80px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'miles', 'body_type', 'is_featured')

    # clickable
    list_display_links = ('id', 'thumbnail', 'car_title')

    # click from outside
    list_editable = ('is_featured',)

    search_fields = ('id', 'car_title', 'city', 'model')

    list_filter = ('city', 'model',)
admin.site.register(Car, CarAdmin)
