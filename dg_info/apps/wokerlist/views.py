from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Status, Position, Department, Group, Adres, Staff, BestWorker, StuctureLeader
import datetime
from datetime import timedelta, date
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

        context['lmenu'] = Group.objects.all().prefetch_related(
                    'staff_set')

        return context


class BirthdayView(ListView):
    model = Staff
    context_object_name = 'birthdays'
    queryset = Staff.objects.filter(b_date__month=today.month)
    template_name = 'wokerlist/birthdays.html'

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
                numOfLeader = Staff.objects.filter(name__lt=j).count()
                leaderArrey.append({'a':numOfLeader, 'b':i.changeStyle})

        context['leaderPush'] =leaderArrey
        context['wokers'] = Staff.objects.filter(fired=False, promotion='loos')

        return context