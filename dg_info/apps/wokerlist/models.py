from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField('добавить статус', max_length=300,
                            help_text='к примеру в отпуске/уволен/работает')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы '
    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('Должность', max_length=300)

    class Meta:
        verbose_name = 'Должности'
        verbose_name_plural = 'Должность'

    def __str__(self):
        return self.name



class Department(models.Model):
    name = models.CharField('Название департамента', max_length=300)

    class Meta:
        verbose_name = 'Департаменты'
        verbose_name_plural = 'Департамент'
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField('Название отдела', max_length=300)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Отделы'
        verbose_name_plural = 'Отдел'

    def __str__(self):
        return self.name

class Adres(models.Model):
    name = models.CharField('Адрес ', max_length=300)

    class Meta:
        verbose_name = 'Адреса'
        verbose_name_plural = 'Адрес'

    def __str__(self):
        return self.name


class Staff(models.Model):
    UPPER_CHOISE=(
        ('loos', 'Сотрудник'),
        ('top', 'Руководитель'),
        ('hr', 'HR'),
    )
    name = models.CharField('ФИО сотрудника', max_length=500)
    b_date = models.DateField('Дата рождения')
    start_work_date = models.DateField('Дата приема на работу')
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    adres = models.ForeignKey(Adres, on_delete=models.PROTECT)
    w_mail = models.EmailField('Рабочий e-mail', null=True, blank=True)
    p_mail = models.EmailField('Личный e-mail', null=True, blank=True)
    w_tel = models.CharField('Рабочий телефон', max_length=22, null=True, blank=True)
    с_tel = models.CharField('Корпоративный телефон', max_length=22, null=True, blank=True)
    p_tel = models.CharField('Личный телефон', max_length=22, null=True, blank=True)
    viber = models.CharField('viber', max_length=100, null=True, blank=True)
    telegram = models.CharField('telegram', max_length=100, null=True, blank=True)
    skype = models.CharField('skype', max_length=100, null=True, blank=True)
    leader = models.ManyToManyField('self',  limit_choices_to={'promotion': 'top'},  null=True, blank=True)
    hr = models.ManyToManyField('self',  limit_choices_to={'promotion': 'hr'},  null=True, blank=True)
    hobby = models.TextField('Хобби и интересы', null=True, blank=True)
    promotion = models.CharField('Стастус сотрудника', max_length=20, choices=UPPER_CHOISE, default='loos',
                              help_text='Статсу сотрудника, Сотрудник/Руководильет/HR. \nБудет возможно выбрать в соотвествующих полях')



    class Meta:
        ordering = ['name']
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name