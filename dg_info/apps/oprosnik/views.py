from django.shortcuts import render
from django.views.generic import CreateView
from .models import OneWeekOpros
from .forms import OneWeekOprosForm


class OneWeekOprosView(CreateView):
    model = OneWeekOpros
    form_class = OneWeekOprosForm
    template_name = 'opros/form.html'
    success_url = '/' #reverse_lazy('/')