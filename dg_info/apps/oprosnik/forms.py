from django import forms
from .models import OneWeekOpros

class OneWeekOprosForm(forms.ModelForm):

    class Meta:
        model = OneWeekOpros
        fields =("acquaintance", "firstWeek", "hrWork", "impressions", "leaderAim", "leaderConnect", "leaderFixed", "leaderRadio", "leaderWork", "whatDoIspatal", "workComfort", "workPlace", "whyDG",)
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': _('ПІБ'), 'class': 'form-control'}),
        #     'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'class': 'form-control'}),
        #     'summ': forms.NumberInput(attrs={'placeholder': _('Стягнута сума, грн *'), 'class': 'form-control'}),
        #     'region': forms.Select(attrs={'class': 'form-control'}),
        #     'penalty': forms.Select(attrs={'class': 'form-control'}),
        #     'about': forms.Textarea(attrs={'placeholder': _('Короткий опис ситуації'), 'class': 'form-control'}),
        #     # 'comments': forms.Textarea(attrs={'placeholder': _('Опишите ваш заказ')}),
        #
        # }
        # labels = {
        #     'name': '',
        #     'email': '',
        #     'tel': '',
        #     'comments': '',
        #     'region':_('выберет регион'),
        # }