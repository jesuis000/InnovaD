from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    numbers = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ['name', 'numbers']
