from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import ContractorsCategory, Contractors, AditionalField


class ContractorsCategoryListView(ListView):
    model = ContractorsCategory
    slug_field = 'id'
    context_object_name = 'Contractors'
    template_name = 'contractors/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['l_ContractorsCategory'] = ContractorsCategory.objects.all()#.prefetch_related('staff_set')
        return context

class ContractorsCategoryDetailView(DetailView):
    model = ContractorsCategory
    # slug_field = 'pk'
    context_object_name = 'Category'
    template_name = 'contractors/contractor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['l_contrmenu'] = ContractorsCategory.objects.all()  # .prefetch_related('staff_set')
        context['contractors'] = Contractors.objects.filter(category_id=self.object.id)
        context['l_category'] = ContractorsCategory.objects.all()
        return context


class ContractorsDetailView(DetailView):
    model = Contractors
    slug_field = 'pk'
    context_object_name = 'Contractor'
    template_name = 'contractors/contractor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aditional'] = AditionalField.objects.filter(contractors_id=self.object.id)
        context['l_contrmenu'] = Contractors.objects.filter(category=self.object.category.id)
        context['l_category'] = ContractorsCategory.objects.all()

        return context


# class ContractorsListView(ListView):
#     model = Contractors
#     # slug_field = 'id'
#     context_object_name = 'Contractors'
#     template_name = 'contractors/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['l_ContractorsCategory'] = ContractorsCategory.objects.all()#.prefetch_related('staff_set')
#         return context