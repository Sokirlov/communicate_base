from django.contrib import admin
from .models import Status, Position, Department, Group, Adres, Staff, BestWorker


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
    list_display = ('name',  'group', 'position', 'work_status', 'b_date', 'start_work_date', 'adres',)
    list_display_links = ('name',)
    list_editable = ('work_status',)
    list_filter = ['start_work_date', 'group', 'adres', ]
    search_fields = ['name',]
    readonly_fields = ('image_tag',)
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields':
             (('name', 'promotion',  'start_work_date',),
              ('work_status', 'replacement_employee'),
              ('group', 'position', 'adres',),
              ('image_tag', 'avatar',),
               ('w_mail',  'w_tel', 'с_tel',),
              ('leader', 'hr',),
              )}
              #('p_tel', 'p_mail','viber', 'telegram', 'skype',), 'leader',  'promotion', 'hobby')}
         ),
        ('Личные данные', {'fields':('b_date', ('p_tel', 'p_mail', 'viber', 'telegram', 'skype',), 'hobby')}),
    )
    class Media:
        js = (
            '/static/js/admin.js',
            '/static/js/jquery-3.6.0.js',
        )

admin.site.register(Staff, StaffAdmin)


class BestWorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'idSort', 'nominate',)
    list_display_links = ('nominate',)
    list_editable = ('idSort',)
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
admin.site.register(BestWorker, BestWorkerAdmin)
