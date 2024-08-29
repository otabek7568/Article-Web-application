from django import forms
from index.models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['mail']