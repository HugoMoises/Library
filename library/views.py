from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Livro
from .forms import LivroForm
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'livros/index.html'

class LivroListView(ListView):
    template_name = 'livros/livros_list.html'
    model = Livro
    context_object_name = 'livros'

class LivroCreateView(CreateView):
    model = Livro
    template_name = 'livros/livro_create.html'
    form_class = LivroForm
    success_url = reverse_lazy('livros_list')

class LivroUpdateView(UpdateView):
    model = Livro
    template_name = 'livros/livro_update.html'
    form_class = LivroForm
    success_url = reverse_lazy('livros_list')

class LivroDetailView(DetailView):
    template_name = 'livros/livro_detail.html'
    model = Livro
    context_object_name = 'livro'

class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('livros_list')






