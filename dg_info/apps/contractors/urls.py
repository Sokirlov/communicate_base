from django.urls import path
from .views import ContractorsCategoryDetailView, ContractorsDetailView, ContractorsCategoryListView #ContractorsListView,

app_name = 'contractors'

urlpatterns = [
    path('', ContractorsCategoryListView.as_view(), name='contractors_main'),
    path('<slug:pk>/', ContractorsCategoryDetailView.as_view(), name='contractors_category'),
    path('<slug:category>/<slug:pk>/', ContractorsDetailView.as_view(), name='contractor_detail'),

]