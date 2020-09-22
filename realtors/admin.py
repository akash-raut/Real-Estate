from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    ''' Includes extra fields to display in admin page '''
    list_display = ['id', 'name', 'email', 'hire_date']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_per_page = 10
    ordering = ['hire_date']


admin.site.register(Realtor, RealtorAdmin)


