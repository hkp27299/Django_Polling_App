from django import forms
from .models import createPoll
class createPollForm(forms.ModelForm):
    class Meta:
        model = createPoll
        fields = ['title','options']
        
