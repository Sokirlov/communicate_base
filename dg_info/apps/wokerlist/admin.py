from django.contrib import admin
from .models import Status, Position, Department, Group, Adres, Staff


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(Status, StatusAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(Position, PositionAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(Department, DepartmentAdmin)

class AdresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(Adres, AdresAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'department',)
    list_display_links = ('name',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(Group, GroupAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'b_date', 'start_work_date', 'group', 'position', 'adres',)
    list_display_links = ('name',)
    # list_editable = ()
    list_filter = ['start_work_date', 'group', 'adres', ]
    search_fields = ['name',]
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields':
             (('name', 'start_work_date',  'promotion',),
              ('group', 'position', 'adres',),

               ('w_mail',  'w_tel', 'с_tel',),
              ('hr', 'leader',),
              )}
              #('p_tel', 'p_mail','viber', 'telegram', 'skype',), 'leader',  'promotion', 'hobby')}
         ),
        ('Личные данные', {'fields':('b_date', ('p_tel', 'p_mail', 'viber', 'telegram', 'skype',), 'hobby')}),
    )

admin.site.register(Staff, StaffAdmin)

