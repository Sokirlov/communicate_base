from django.db import models
from wokerlist.models import Staff

class OneWeekOpros(models.Model):
    CHISES_MANY = (
        ('awesome', 'Отлично'),
        ('good', 'Не плохо'),
        ('normal', 'Удовлетворительно'),
        ('bad', 'Плохо'),
        ('awfully', 'Ужасно'),
    )
    CHISES_YES_NO = (
        ('yes', 'Да'),
        ('no', 'Нет'),
    )
    dateAnsvered = models.DateTimeField(auto_now_add=True)
    whyDG = models.CharField('Почему Вы выбрали именно нашу компанию?', max_length=1000)
    hrWork = models.CharField('Ваше впечатление от взаимодействия с HR на этапе предложения о работе и собеседования.',
                              choices=CHISES_MANY, max_length=10)
    leaderWork = models.TextField('Ваше впечатление от взаимодействия с непосредственным руководителем на этапе собеседования.',
                                  help_text='оцените от 1 до 10, также необходимо прокомментировать оценку')
    acquaintance = models.CharField('Как прошло знакомство с коллективом?',
                                    choices=CHISES_MANY, max_length=10)
    impressions = models.TextField('Ваши впечатления от коллектива?')
    workPlace = models.CharField('Ваши впечатления от коллектива?',
                                 choices=CHISES_YES_NO, max_length=5)
    whatDoIspatal = models.CharField('Понятен ли Вам функционал? Чем необходимо заниматься в период испытательного срока?',
                                     choices=CHISES_YES_NO, max_length=5)
    leaderConnect = models.CharField('Мой руководитель дает мне эффективную обратную связь, которая помогает мне улучшить свою работу.',
                                     choices=CHISES_MANY, max_length=10)
    leaderFixed = models.CharField('За Вами закреплён наставник?',
                                   help_text='имеется в виду человек, у которого Вы можете спросить, уточнить, узнать необходимую информацию',
                                   choices=CHISES_YES_NO, max_length=5)
    leaderAim = models.CharField('Мой руководитель держит команду сфокусированной на приоритетных результатах/конечном результате.',
                                help_text='имеется в виду человек, у которого Вы можете спросить, уточнить, узнать необходимую информацию',
                                choices=CHISES_MANY, max_length=10)
    leaderRadio = models.CharField('Мой руководитель транслирует ясные цели для нашей команды.',
                                   help_text='имеется в виду человек, у которого Вы можете спросить, уточнить, узнать необходимую информацию',
                                   choices=CHISES_MANY, max_length=10)
    workComfort = models.CharField('Вас устраивает организация условий труда?',
                                   help_text='качество осветления, температура в помещении, общее впечатления от офиса',
                                   choices=CHISES_YES_NO, max_length=5)
    firstWeek = models.CharField('Как прошла Ваша первая рабочая неделя?',
                                 help_text='имеется в виду передали Вам необходимую информацию и инструменты для выполнения',
                                 choices=CHISES_YES_NO, max_length=5)
    user = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['-dateAnsvered']
        verbose_name = 'Опрос первой недели'
        verbose_name_plural = 'Опрос первой недели'

    def __str__(self):
        return str(self.dateAnsvered)