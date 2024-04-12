from django.contrib import admin
from .models import Service, BookedService

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description') 

admin.site.register(Service, ServiceAdmin)

class BookedServiceAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'service_date', 'additional_notes')

admin.site.register(BookedService, BookedServiceAdmin)