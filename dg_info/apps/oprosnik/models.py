from django.db import models
from wokerlist.models import Staff
import datetime


class Quith(models.Model):
    date_crearte = models.DateField('Дата создания', auto_now_add=True)
    name = models.CharField('Название опроса', max_length=120)
    slug = models.SlugField('URL для опроса', max_length=125)
    # questions = models.ForeignKey(Quessions, verbose_name='Вопросы', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-date_crearte']
        verbose_name = 'Опросы'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'{self.name}'

class Quessions(models.Model):
    question = models.CharField('Вопрос', max_length=300)
    idsort = models.PositiveSmallIntegerField('Порядок сортировки', default=0)
    # answer = models.ForeignKey(VariantsAnswer, on_delete=models.DO_NOTHING)
    quith = models.ForeignKey(Quith, verbose_name='Опрос', on_delete=models.CASCADE, null=True, )

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question

class VariantsAnswer(models.Model):
    answer = models.CharField('Вариант ответа', max_length=300, null=True, blank=True)
    idsort = models.PositiveSmallIntegerField('Порядок сортировки', default=0, null=True, blank=True)
    questions = models.ForeignKey(Quessions, verbose_name='Вопросы', on_delete=models.CASCADE, null=True,)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Варианты ответа'
        verbose_name_plural = 'Варианты ответа'
    def __str__(self):
        return f'{self.answer}'

def names():
    return str(datetime.datetime.now().timestamp())


class Interviewed(models.Model):
    userName = models.CharField('Имя', max_length=250, default=names)
    user = models.ForeignKey(Staff, on_delete=models.DO_NOTHING, null=True, blank=True)
    # quith = models.ForeignKey(Quith, on_delete=models.DO_NOTHING, null=True, blank=True)
    # questions = models.ForeignKey(Quessions, on_delete=models.DO_NOTHING, null=True, blank=True)
    # answer = models.ForeignKey(VariantsAnswer, on_delete=models.DO_NOTHING, null=True, blank=True)
    # writeAnswer = models.CharField('Ответ клиента', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Респонденты'
        verbose_name = 'Респонденты'
    def __str__(self):
        return self.userName


class InterviewedAnswer(models.Model):
    userName = models.ForeignKey(Interviewed, on_delete=models.CASCADE, null=True, blank=True)
    quith = models.ForeignKey(Quith, on_delete=models.DO_NOTHING, null=True, blank=True)
    questions = models.ForeignKey(Quessions, on_delete=models.DO_NOTHING, null=True, blank=True)
    answer = models.ForeignKey(VariantsAnswer, on_delete=models.DO_NOTHING, null=True, blank=True)
    writeAnswer = models.CharField('Ответ клиента', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Ответы респондентов'
        verbose_name = 'Ответы респондентов'
    def __str__(self):
        return f'{self.quith}'
