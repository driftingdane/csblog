from django.contrib import admin

# Register your models here.
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'message', 'email', 'contact_date')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'email', 'message')
	list_per_page = 25
