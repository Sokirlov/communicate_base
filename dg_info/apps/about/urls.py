from django.urls import path
# from .views import AboutTextView
from . import views

app_name = 'about'

urlpatterns = [
    # path('', AboutTextView.as_view(), name='company-info'),
    path('', views.AboutTextView, name='company-info'),
    ]