from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(text)

@register.filter(name='calTry')
def calendar_tray_day(cal_day, b_day):
    print('cal_day', cal_day)
    print('b_day ', b_day)