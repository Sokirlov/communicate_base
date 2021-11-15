from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from .models import VariantsAnswer, Quessions, Quith, InterviewedAnswer, Interviewed




class VariantsAnswerAdmin(NestedTabularInline):
    model = VariantsAnswer
    extra = 0
    ordering = ['idsort', ]
    sortable_field_name = ['idsort', ]
    list_editable = ['idsort', ]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)


class QuessionsAdmin(NestedStackedInline):
    model = Quessions
    extra = 0
    ordering = ['idsort', ]
    sortable_field_name = ['idsort', ]
    list_editable = ['idsort', ]
    classes = ('grp-collapse grp-closed',)
    inline_classes = ('grp-collapse grp-closed',)
    inlines = [VariantsAnswerAdmin]



class QuithAdmin(NestedModelAdmin):
    list_display = ('date_crearte', 'name',)
    list_display_links = ('date_crearte', 'name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [QuessionsAdmin, ]
admin.site.register(Quith, QuithAdmin)


class InterviewedAnswer(admin.TabularInline):
    model = InterviewedAnswer
    extra = 0
    readonly_fields = ['quith', 'questions', 'answer', 'writeAnswer']

class InterviewedAdmin(admin.ModelAdmin):
    list_display = ('userName',)
    list_display_links = ('userName',)
    inlines = [InterviewedAnswer, ]
admin.site.register(Interviewed, InterviewedAdmin)