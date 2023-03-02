from django import forms
from django.contrib.auth.models import User
from .models import User
from base.constance import Role


class UserCreate(forms.ModelForm):
    role = forms.ChoiceField(choices=Role.choices())
    class Meta:
        model = User
        fields = ['username','email','role','password']

    def clean(self):
        '''clean method for email'''
        super().clean()

    def save(self, commit=False):
        instance = super().save(commit=True)
        if commit:
            instance.save()
        return instance
