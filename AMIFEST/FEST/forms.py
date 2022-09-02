from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, fields
from .models import user_registration



class usersform(ModelForm):
    class Meta:
        model = user_registration
        fields = ('first_name', 'last_name', 'email', 'block', 'branch', 'phone_number', 'university')

        labels={
             'first_name': '',
            'last_name': '',
            'email': '',
            'block': '',
            'branch': '',
            'phone_number': '',
            'university': '',

      
        }


        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':' First Name' }),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'} ),
            'block': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Block Name to get updates on or choose all'}),
            'branch': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Branch\Course'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'university': forms.TextInput(attrs={'class':'form-control', 'placeholder':'University\College'}),

        }
