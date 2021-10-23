from django.core.mail import send_mail, send_mass_mail


import time
import asyncio




def sending_mails_for_workers(mails, subject, message, atach=None):
    # print('start sending emails')
    messages = []
    # send_mail(subject, message, 'info@anticollect.org', ['k.sokolov@dgfinance.com.ua',], html_message=message)
    for i in mails:
        # send_mail(subject, message, 'dg_info@dgfinance.com.ua', [i], html_message=message)
        messages.append((subject, message, 'dg_info@dgfinance.com.ua', [i,]))
    send_mass_mail(messages)
    # print(messages)

    # print('done')

