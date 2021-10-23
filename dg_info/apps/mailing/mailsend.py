from django.core.mail import send_mail, send_mass_mail
import re

import time
import asyncio
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail

#
#
# def sending_mails_for_workers(mails, subject, raw_message, atach=None):
#     html_message = raw_message
#     message = re.sub(r'\<[^>]*\>', '', raw_message)
#     messages = []
#     # send_mail(subject, message, 'info@anticollect.org', ['k.sokolov@dgfinance.com.ua',], html_message=message)
#     for i in mails:
#         # send_mail(subject, message, 'dg_info@dgfinance.com.ua', [i], html_message=message)
#         messages.append((subject, message, 'dg_info@dgfinance.com.ua', [i,], ))
#     # send_mass_mail(messages)
#     print(messages)

def sending_mails_for_workers(mails, subject, raw_message, atach=None):
    html_message = raw_message
    message = re.sub(r'\<[^>]*\>', '', raw_message)
    emails = []
    for i in mails:
        email = EmailMultiAlternatives(subject, message, 'dg_info@dgfinance.com.ua', [i,])
        email.attach_alternative(html_message, 'text/html')
        # email.attach(atach.name,  atach.content_type)
        # email.attach_file(atach)
        emails.append(email)
    return get_connection().send_messages(emails)
