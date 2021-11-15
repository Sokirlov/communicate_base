from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Interviewed, InterviewedAnswer, Quith, Quessions
from .forms import OprosForm
import datetime


class QuizView(ListView):
    model = Quith
    slug_field = 'slug'
    context_object_name = 'quiz'
    paginate_by = 20
    template_name = 'opros/main.html'


def QuessionsV(request, **kwargs):
    quiz =Quith.objects.filter(slug=kwargs['slug']).prefetch_related('quessions_set', 'quessions_set__variantsanswer_set')
    userName = str(datetime.datetime.now().timestamp())
    quithnum = Quith.objects.get(slug=kwargs['slug'])
    username = str(datetime.datetime.now().timestamp())
    if request.method == "POST":
        formset = request.POST
        instance = formset.copy()
        Interviewed.objects.update_or_create(userName=username)
        respondet = Interviewed.objects.get(userName=username)

        del instance['csrfmiddlewaretoken']
        for i, j in instance.items():
            if len(j) > 2:
                b = j
                a = None
            else:
                b = None
                a = j
            quesId = Quessions.objects.get(question=i).id
            InterviewedAnswer.objects.create(userName_id=respondet.id,
                                             quith_id=quithnum.id,
                                             questions_id=quesId,
                                             answer_id=a,
                                             writeAnswer=b,
                                             )
            # print('OK', i, j)
            # return HttpResponseRedirect(quiz.get_absolute_url())
    else:
        formset = OprosForm()
    return render(request, 'opros/quessions.html', {'quessions':quiz, "form": formset})