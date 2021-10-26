from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail, send_mail
from wokerlist.models import Staff
from mailing.models import Birthday
import datetime

templates_mails = Birthday.objects.all()




class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(templates_mails) > 0:
            t_mail = templates_mails.get()
            subject = t_mail.subject
            message = t_mail.message
            today = datetime.date.today()
            be_beathday = Staff.objects.filter(b_date=today)
            # messages = []
            # for i in be_beathday:
            #     messages.append((subject, message, 'dg_info@dgfinance.com.ua', [i.w_mail, ],))
            # send_mass_mail(messages)

            # print('It`s sended ', t_mail.subject, t_mail.message)
            send_mail(subject, message, 'dg_info@dgfinance.com.ua', ['k.sokolov@dgfinance.com.ua'])