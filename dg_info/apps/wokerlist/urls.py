from django.urls import path
from .views import GroupListView, GroupDetailView, StaffDetailView

app_name = 'wokerlist'

urlpatterns = [
    path('', GroupListView.as_view(), name='adresBook'),
    path('<slug:pk>/', GroupDetailView.as_view(), name='group-staff'),
    path('<slug:group__id>/<slug:pk>/', StaffDetailView.as_view(), name='staffView'),

]