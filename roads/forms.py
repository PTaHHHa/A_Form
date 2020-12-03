from .models import CitizenAppeal
from django import forms


class CitizenAppealForm(forms.ModelForm):
    class Meta:
        model = CitizenAppeal
        fields = '__all__'
