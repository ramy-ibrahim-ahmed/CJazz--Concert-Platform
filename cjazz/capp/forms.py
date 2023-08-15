from django import forms
from django.forms import ModelForm
from .models import Contact, Ticket

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email', 
            'company', 
            'message',
        )

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'full name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}), 
            'company':forms.TextInput(attrs={'class':'form-control', 'placeholder':'company'}), 
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'enter your message', 'rows':'3'}),
        }

        labels = {
            'name':'',
            'email':'', 
            'company':'', 
            'message':'',
        }

#----------------------------------------------------------------------------------

class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = (
            'name',
            'email', 
            'phone', 
            'plan', 
            'party',
            'number',
        )

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'full name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}), 
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}), 
            'plan':forms.Select(attrs={'class':'form-select', 'placeholder':'Ticket Type'}),
            'party':forms.Select(attrs={'class':'form-select', 'placeholder':'Party'}),
            'number':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of tickets', 'min': '1'}),
            'feedback':forms.Textarea(attrs={'class':'form-control', 'placeholder':'enter your message', 'rows':'3'}),
        }

        labels = {
            'name':'',
            'email':'',
            'phone':'',
            'plan':'Ticket Type',
            'party':'Party', 
            'number':'', 
            'feedback':'',
        }