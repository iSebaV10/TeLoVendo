from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
