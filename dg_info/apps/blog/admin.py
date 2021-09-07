from django.contrib import admin
from .models import BlogCategory, Posts

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'idSort',)
    list_display_links = ('id', 'category',)
    list_editable = ('idSort',)
    prepopulated_fields = {'slug': ('category',),}
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(BlogCategory, BlogCategoryAdmin)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'category', 'created', 'publicate',)
    list_display_links = ('id', 'name',)
    list_editable = ('publicate',)
    prepopulated_fields = {'slug': ('name',),}
    readonly_fields = ('created', 'edited',)
    list_filter = ['category',]
    search_fields = ['name',]
    fieldsets = (('Разработано Sokolov for DG Finance',{'fields':(
        ('category', 'publicate',),
        ('name', 'slug',),
        ('created', 'edited',),
        'text',
    ),},),)
admin.site.register(Posts, PostsAdmin)
