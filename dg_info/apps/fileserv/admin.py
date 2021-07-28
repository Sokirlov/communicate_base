from django.contrib import admin
from .models import HRDocs

class HRDocsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_create', 'name')
    list_display_links = ('id', 'date_create', 'name')
    readonly_fields = ('date_create',)
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {
            'fields': (('name', 'date_create'), 'filedoc',),}),)

admin.site.register(HRDocs, HRDocsAdmin)
