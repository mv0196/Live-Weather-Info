from django import forms
from .models import City,UserData
from django.core import validators

def nameValid(value):
    if value != value.title():
        raise forms.ValidationError("Name must Write as Title (eg: Las Vegas)")
    return nameValid

class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City Name...'}), validators=[nameValid])

    class Meta:
        model = City
        fields = ['name']

class UserForm(forms.ModelForm):


    class Meta():
        model = UserData
        fields = '__all__'

    
    #def clean(self):
    #    cleanData = super().clean()
    #    age = cleanData['Age']
    #     if len(age) == 2 or age =='e' or age == 'ee':
    #         raise forms.ValidationError("!! You Are Under Age !!")
