from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['title', 'author', 'gender', 'publication_year', 'avaiable', 'cover']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender' : forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year' : forms.NumberInput(attrs={'class': 'form-control'}),
            'avaiable' : forms.NumberInput(attrs={'class': 'form-control'}),
            'cover' : forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }