from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Status, Position, Department, Group, Adres, Staff, BestWorker, StuctureLeader

import datetime
from django.db.models import Q
from datetime import timedelta, date
from haystack.query import SearchQuerySet

today = datetime.date.today()


class GroupListView(ListView):
    model = Staff
    slug_field = 'id'
    context_object_name = 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lmenu'] = Group.objects.all().prefetch_related(
            'staff_set')

        return context

class SearchResultsView(ListView):
# def SearchResultsView(request):
    model = Staff
    # slug_field = 'id'
    context_object_name = 'staff'
    template_name = 'search/search.html'
    # form_class = SearchForm
    # queryset = SearchQuerySet().filter(content='Соколов')


    def get_queryset(self):
        query = self.request.GET.get('q')
        staff = SearchQuerySet().models(Staff).filter(content__startswith=query).load_all()
        return staff
    # return render(request, 'search/search.html', {'staff': queryset, 'allStaff': allStaff})

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lmenu'] = Group.objects.all().prefetch_related('staff_set')
        # context['search'] =SearchQuerySet().filter(content=(self.request.GET.get('q'))).load_all()
        # print('last', context['search'].query.model)
        return context

class GroupDetailView(DetailView):
    model = Group
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Staff.objects.filter(group=self.get_object())
        context['lmenu'] = Group.objects.all()
        return context

class StaffDetailView(DetailView):
    model = Staff
    slug_field = 'pk'
    context_object_name = 'staff'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lmenu'] = Group.objects.all().prefetch_related('staff_set')
        return context


class BirthdayView(ListView):
    model = Staff
    context_object_name = 'birthdays'
    queryset = Staff.objects.filter(b_date__month=today.month)
    template_name = 'wokerlist/birthdays.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        firstDayOfMonth = today.replace(day=1)
        lastDayOfMonth = today.replace(month=today.month + 1, day=1) - datetime.timedelta(days=1)
        DaysOfMonth = []
        for i in range(firstDayOfMonth.day, lastDayOfMonth.day+1):
            day = "{:02d}".format(i)
            DaysOfMonth.append(day)

        for j in range(1, firstDayOfMonth.isoweekday()):
            DaysOfMonth.insert(0, 0)

        NewMonthes = []
        first = 0
        last = 7
        for h in range(1, 6):
            weekss = []
            for k in DaysOfMonth[first:last]:
                weekss.append(k)
            first += 7
            last += 7
            NewMonthes.append(weekss)


        context['DayOfMonth'] = NewMonthes
        print(NewMonthes)
        return context

class BestWorkerView(ListView):
    model = BestWorker
    context_object_name = 'bestwokers'
    queryset = BestWorker.objects.all()
    template_name = 'wokerlist/best.html'

class Structure(ListView):
    model = Staff
    slug_field = 'id'
    context_object_name = 'structure'
    template_name = 'wokerlist/structure.html'
    queryset = Staff.objects.filter(fired=False).exclude(promotion='loos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # allStuctureLeader.objects.all()
        leaderArrey = []
        for i in StuctureLeader.objects.all():
            for j in i.leader.all():
                numOfLeader = Staff.objects.filter(name__lt=j, fired=False).exclude(promotion='loos').count()
                leaderArrey.append({'a':numOfLeader, 'b':i.changeStyle})
        context['leaderPush'] =leaderArrey
        context['wokers'] = Staff.objects.filter(fired=False, promotion='loos')

        return context