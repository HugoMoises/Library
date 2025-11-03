from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Livro, Emprestimo

User = get_user_model()

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

#Empréstimo
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

class EmprestimoStatusForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['status']

        widgets = {
            'status' : forms.Select(attrs={'class': 'form-control'}),
        }

    

# Registro de Usuário
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }