from .models import DemoRegister
from django import forms
class DemoRegisterForm(forms.ModelForm):
    class Meta:
        model=DemoRegister
        fields='__all__'
