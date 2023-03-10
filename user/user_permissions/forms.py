from django import forms
from django.contrib.auth.models import User,Group
from .models import User,Manufacturer
from base.constance import Role


class LoginForm(forms.ModelForm):
    '''login form '''
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        '''login form meta class'''
        model = User
        fields = ['email','password']

class UserCreate(forms.ModelForm):
    role = forms.ChoiceField(choices=Role.choices())
    class Meta:
        model = User
        fields = ['username','email','role']

    def save(self, commit=False):
        print("dafasudsaydfsaygdfisuadfsagfsafysfuiosdgfsdukgio")
        instance = super().save(commit=True)
        instance.set_password(instance.username +'@1234')
        if commit:
            instance.save()
        return instance

class EditUser(forms.ModelForm):
    role = forms.ChoiceField(choices=Role.choices())
    class Meta:
        model = User
        fields = ['username','email','role']

class CreateItems(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name','quantity'] 