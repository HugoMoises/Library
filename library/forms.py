from django import forms
from .models import Livro, Emprestimo

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


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['person', 'book', 'return_date', 'status']

        widgets = {
            'person' : forms.Select(attrs={'class': 'form-control'}),
            'book' : forms.Select(attrs={'class': 'form-control'}),
            'return_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
        }