from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TalabaForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=30, label="Ism:")
    nums_of_books = forms.IntegerField(min_value=0, max_value=10, label="Kitob soni:")
    course = forms.IntegerField(min_value=1, max_value=4, label="Kurs:")
    senior = forms.BooleanField(required=False, initial=True, label="Bitruvchi:")

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ('__all__')

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = ('__all__')
        widgets = {'tugilgan_yil': DateInput()}

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {'olingan_sana': DateInput(), 'qaytargan_sana': DateInput()}

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
