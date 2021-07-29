from django.db import models
from django.utils.safestring import  mark_safe
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Status(models.Model):
    name = models.CharField('добавить статус', max_length=300,
                            help_text='к примеру в отпуске/уволен/работает')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = '2.7. Статусы'
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField('Должность', max_length=300)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = '2.6. Должности'

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField('Название департамента', max_length=300)

    class Meta:
        verbose_name = 'Департаменты'
        verbose_name_plural = '2.3. Департаменты'
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField('Название отдела', max_length=300)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = '2.4. Отделы'

    def __str__(self):
        return self.name

class Adres(models.Model):
    name = models.CharField('Адрес ', max_length=300)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = '2.5. Адреса'

    def __str__(self):
        return self.name


class Staff(models.Model):
    UPPER_CHOISE=(
        ('loos', 'Сотрудник'),
        ('top', 'Руководитель'),
        ('hr', 'HR'),
    )
    STATUS_CHOISE = (
        ('InWork', 'На работе'),
        ('vocation', 'В отпуске'),
        ('seek', 'На больничном'),
        ('wfh', 'Работает с дома'),
    )
    name = models.CharField('ФИО сотрудника', max_length=500)
    b_date = models.DateField('Дата рождения', blank=True, null=True)
    start_work_date = models.DateField('Дата приема на работу')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Отдел')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='Должность')
    adres = models.ForeignKey(Adres, on_delete=models.PROTECT, verbose_name='Адрес')
    w_mail = models.EmailField('Рабочий e-mail', null=True, blank=True)
    p_mail = models.EmailField('Личный e-mail', null=True, blank=True)
    w_tel = models.CharField('Рабочий телефон', max_length=22, null=True, blank=True)
    с_tel = models.CharField('Корпоративный телефон', max_length=22, null=True, blank=True)
    p_tel = models.CharField('Личный телефон', max_length=22, null=True, blank=True)
    viber = models.CharField('viber', max_length=100, null=True, blank=True)
    telegram = models.CharField('telegram', max_length=100, null=True, blank=True)
    skype = models.CharField('skype', max_length=100, null=True, blank=True)
    leader = models.ForeignKey('self',  blank=True, null=True, on_delete=models.PROTECT,
                               limit_choices_to={'promotion': 'top'}, related_name='Leader', verbose_name='Руководитель')
    hr = models.ForeignKey('self', limit_choices_to={'promotion': 'hr'}, blank=True, null=True, on_delete=models.PROTECT , related_name='HR')
    hobby = RichTextUploadingField('Хобби и интересы', null=True, blank=True)
    promotion = models.CharField('Позиция сотрудника', max_length=20, choices=UPPER_CHOISE, default='loos',
                              help_text='Статсу сотрудника, Сотрудник/Руководильет/HR. \nБудет возможно выбрать в соотвествующих полях')
    avatar = models.ImageField('Фото сотрудника', upload_to='photo/sotrudniki', null=True, blank=True)
    work_status = models.CharField(choices=STATUS_CHOISE, max_length=500, verbose_name='Состояние, статус', default='В работе', null=True, blank=True)
    replacement_employee = models.ForeignKey('self',  blank=True, null=True, on_delete=models.PROTECT,
                               # limit_choices_to={'promotion': 'top'},
                                             related_name='r_staf', verbose_name='Замена')
    def get_absolute_url(self):
        return reverse('wokerlist:staffView', kwargs={'group__id': self.group.id, 'pk': self.pk})

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" />' % (self.avatar))
    image_tag.short_description = 'Фото'


    class Meta:
        ordering = ['name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = '2.2. Сотрудники'

    def __str__(self):
        return self.name

class BestWorker(models.Model):
    nominate = models.CharField('Номинация', max_length=500, default='Лучший сотрудник')
    idSort = models.SmallIntegerField('Сортировка', default='0')
    staff = models.ManyToManyField(Staff)

    class Meta:
        ordering = ['idSort']
        verbose_name = 'Лучший сотрудник'
        verbose_name_plural = '2.1. Лучшие сотрудники'

    def __str__(self):
        return self.nominate