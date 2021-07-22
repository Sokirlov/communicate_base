from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import AboutText

# class AboutTextView(DetailView):
#     model = AboutText
#     context_object_name = 'about'
#     template_name = 'about/index.html'


def AboutTextView(request):
    about = AboutText.objects.all()
    return render(request, 'about/index.html', {'about': about})