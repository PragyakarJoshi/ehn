from django.contrib import admin
from .models import Category, Event

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "category_description"]
    display_links = ["category_name", "category_description"]

    class Meta: 
        model = Category

class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "location"]
    display_links = ["title", "date", "location"]

    class Meta: 
        model = Event

admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
