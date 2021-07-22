from django.contrib import admin
from .models import ContractorsCategory, Contractors, AditionalField

class AditionalFieldInline(admin.TabularInline):
# class AditionalFieldInline(admin.StackedInline):

    model = AditionalField
    extra = 0
    # ordering = ['idsort',]
    list_editable = ['idsort', 'name', 'valuefield']
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    # sortable_field_name = "idsort"
    fieldsets = (('Дополнительные поля',{'fields': (
        'idSort',  'name', 'valuefield', 'contractors'
    ), }),)

class ContractorsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    list_display_links =['id', 'category',]
    fieldsets = (('Разработано Sokolov Kyrylo of DG Finance',{'fields': ('category',)}),)
admin.site.register(ContractorsCategory, ContractorsCategoryAdmin)



class ContractorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_edit', 'category', 'title',)
    list_display_links =['last_edit','title',]
    list_filter = ['category']
    fieldsets = (('Разработано Sokolov Kyrylo of DG Finance',{'fields': (
        # 'last_edit',
                                                                         ('title', 'category',),
                                                                         ('tel', 'email',),
                                                                         'adr',
                                                                         )}),)
    # readonly_fields = ('last_edit',)
    inlines = [
        AditionalFieldInline
    ]

admin.site.register(Contractors, ContractorsAdmin)