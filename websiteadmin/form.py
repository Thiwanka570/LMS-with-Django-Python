from django import forms
from .models import members
from .models import books

class UpdateMembersForm(forms.ModelForm):
    name=forms.CharField(max_length=100,widget=forms.TextInput())
    contact=forms.CharField(max_length=10,widget=forms.TextInput())
    email=forms.CharField(max_length=200,widget=forms.TextInput())
        
    class Meta():
        model = members
        fields = ['name', 'contact', 'email']


class UpdateBooks(forms.ModelForm):
    name=forms.CharField(max_length=100,widget=forms.TextInput())
    title=forms.CharField(max_length=10,widget=forms.TextInput())
    subject=forms.CharField(max_length=200,widget=forms.TextInput())
    publisher=forms.CharField(max_length=200,widget=forms.TextInput())
    author=forms.CharField(max_length=200,widget=forms.TextInput())

        
    class Meta():
        model = books
        fields = ['name', 'title', 'subject','publisher','author']
        
