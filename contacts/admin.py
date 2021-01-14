from django.contrib import admin

# Register your models here.
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'create_date')

    # clickable
    list_display_links = ('id', 'first_name', 'last_name')

    search_fields = ('first_name', 'last_name', 'email', 'car_title')

    list_per_page = 25


admin.site.register(Contact, ContactAdmin)