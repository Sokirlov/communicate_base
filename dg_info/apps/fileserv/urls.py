from django.urls import path
from .views import HRDocsView

app_name = 'fileserv'

urlpatterns = [
    path('', HRDocsView.as_view(), name='main'),

]