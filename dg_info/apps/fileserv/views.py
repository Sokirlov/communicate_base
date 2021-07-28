from django.shortcuts import render
from .models import HRDocs
from django.views.generic.list import ListView

class HRDocsView(ListView):
    model = HRDocs
    context_object_name = 'hrdocs'
    template_name = 'fileserv/index.html'
