from django.core.mail import send_mail, send_mass_mail


import time
import asyncio




def sending_mails_for_workers(mails, subject, message, atach):
    print('start sending emails')
    # emailss = []
    # send_mail(subject, message, 'info@anticollect.org', ['k.sokolov@dgfinance.com.ua',], html_message=message)
    for i in mails:
    #     send_mail(titles, text, 'info@anticollect.org', [i], html_message=text)
        send_mail(subject, message, 'info@anticollect.org', [i, ], html_message=message)
        # emailss.append(message)
    # print('ready for send - ', emailss)

    # send_mass_mail(emailss)
    print('done')
    # email = EmailMessage()
    #
    # print('mails', mails)
    # print('titles', titles)
    # print('text', text)
    # print('atach', atach)

