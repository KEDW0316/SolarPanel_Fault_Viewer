from django import forms
from .models import panel_fault


class FaultForm(forms.ModelForm):
    class Meta:
        model=panel_fault
        fields=('px_x','px_y')