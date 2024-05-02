from django import forms
from .models import Boys, Girls

class BoysForm(forms.ModelForm):
    class Meta:
        model = Boys
        fields = ['time']
        widgets = {'time': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S')}
        input_formats = ['%Y-%m-%d %H:%M:%S.%f']


class GirlsForm(forms.ModelForm):
    class Meta:
        model = Girls
        fields = ['time']
        widgets = {'time': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S')}
    input_formats = ['%Y-%m-%d %H:%M:%S.%f']
