from django.urls import path
from .views import OneWeekOprosView

app_name = 'oprosnik'

urlpatterns = [
    path('', OneWeekOprosView.as_view(), name='oneWeek'),
]