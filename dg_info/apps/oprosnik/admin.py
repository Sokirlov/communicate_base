from django.contrib import admin
from .models import OneWeekOpros

class OneWeekOprosAdmin(admin.ModelAdmin):
    list_display = ('dateAnsvered',)
    list_display_links = ('dateAnsvered',)
    autocomplete_fields = ['user']
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(OneWeekOpros, OneWeekOprosAdmin)
