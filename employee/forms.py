from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import employee
class employeeform(ModelForm):
    class Meta:
        model=employee
        fields='__all__'

        Widget={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
        }