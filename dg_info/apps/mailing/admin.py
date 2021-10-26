from django.contrib import admin
from .models import MailingModel, Birthday
from wokerlist.models import Staff, Group
from .mailsend import sending_mails_for_workers


def get_all_mail():
    email_list = []
    all_staff = Staff.objects.filter(fired=False)
    for i in all_staff:
        if i.w_mail != None:
            email_list.append(i.w_mail)
    return email_list

def get_group_mail(group_name):
    email_list = []
    for i in group_name:
        group = Staff.objects.filter(group=i)
        for j in group:
            if j.w_mail != None:
                email_list.append(j.w_mail)
    return email_list

def gat_users_mail(userslist):
    email_list = []
    for i in userslist:
        if i.w_mail != None:
            email_list.append(i.w_mail)
    return email_list

def prepear_sender_list(obj):
    if obj['all_to_send']:
        mails_list = get_all_mail()
        # print('all emails', mails_list)
    elif len(obj['gorup_to_send']) != 0:
        mails_list = get_group_mail(obj['gorup_to_send'])
        # print('groups emails', mails_list)
    elif len(obj['users_to_send']) != 0:
        mails_list = gat_users_mail(obj['users_to_send'])
        # print('by user emails', mails_list)
    else:
        print('no emails')
    return mails_list



class MailingAdmin(admin.ModelAdmin):
    list_display = ('daite_create', 'title_mail')
    list_display_links = ('daite_create',)
    # list_editable = ()
    # list_filter = ['pub_date']
    # search_fields = ['question_text']
    autocomplete_fields = ['users_to_send']


    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields':
                                                    ("title_mail",
                                                     "text_mail",
                                                     # "file_mail",
                                                     "all_to_send",
                                                     "gorup_to_send",
                                                     "users_to_send",
                                                     "start_send_email")}
         ),
    )

    def save_model(self, request, obj, form, change):
        super(MailingAdmin, self).save_model(request, obj, form, change)
        if form.cleaned_data['start_send_email']:
            sender_list = prepear_sender_list(form.cleaned_data)
            sending_mails_for_workers(sender_list,
                                      form.cleaned_data['title_mail'],
                                      form.cleaned_data['text_mail'],
                                      # form.cleaned_data['file_mail']
                                      )
admin.site.register(MailingModel, MailingAdmin)


class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject')
    list_display_links = ('subject',)
    def has_add_permission(self, request):
        allcontact = len(Birthday.objects.all())
        if(allcontact > 0):
            return False
        else:
            return True

admin.site.register(Birthday, BirthdayAdmin)