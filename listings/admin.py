from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    ''' Includes extra fields to display in admin page and add extra properties '''
    list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor']
    list_display_links = ['id', 'title']
    search_fields = ['realtor']
    ordering = ['id']
    list_filter = ['realtor']
    list_editable = ['is_published']
    list_per_page = 10


admin.site.register(Listing, ListingAdmin)

