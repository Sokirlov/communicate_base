from django import forms
import datetime
from oprosnik.models import Interviewed, InterviewedAnswer, Quith

username = str(datetime.datetime.now().timestamp())

class OprosForm(forms.ModelForm):


    class Meta():
        model = InterviewedAnswer
        fields = '__all__'
        widgets = {
            'userName': forms.TextInput(attrs= {'value': username, 'type': "text", 'readonly':'readonly',}),
        }