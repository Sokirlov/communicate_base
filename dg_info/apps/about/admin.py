from django.contrib import admin
from .models import AboutText

class AboutTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(AboutText, AboutTextAdmin)

