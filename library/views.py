from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Livro
from .forms import LivroForm
# Create your views here.

class IndexView(TemplateView):
    template_name = 'livros/index.html'

class LivroListView(ListView):
    template_name = 'livros/livros_list.html'
    model = Livro
    context_object_name = 'livros'



    