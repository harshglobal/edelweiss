from django import forms
from topper.models import InsertSymbols

class DropdownForm(forms.ModelForm):
    class Meta:
        model = InsertSymbols
        fields  = '__all__'

