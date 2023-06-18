
from django import forms
from .models import Equation

class EquationForm(forms.ModelForm):
    class Meta:
        model = Equation
        fields = ['value_a', 'value_b', 'value_c'] 