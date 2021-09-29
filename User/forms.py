from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'doy', 'gender', 'address', 'phone_no', 'email', 'password', 'suggestion', 'created_date')
