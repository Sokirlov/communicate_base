from django.urls import path
from . import views
from .views import QuizView


app_name = 'oprosnik'

urlpatterns = [
    path('', QuizView.as_view(), name='quiz_main'),
    # path('<slug:slug>/', QuessionsView.as_view(), name='quessions'),
    path('<slug:slug>/', views.QuessionsV, name='quessions')
]