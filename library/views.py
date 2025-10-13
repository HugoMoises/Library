from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Livro, Emprestimo
from .forms import LivroForm, EmprestimoForm
from django.urls import reverse_lazy
# Create your views here.

#Index
class IndexView(TemplateView):
    template_name = 'livros/index.html'

#Livros
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


#Empréstimo
class EmprestimoListView(ListView):
    template_name = 'emprestimos/emprestimos_list.html'
    model = Emprestimo
    context_object_name = 'emprestimos'

class EmprestimoCreateView(CreateView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_create.html'
    form_class = EmprestimoForm
    success_url = reverse_lazy('emprestimos_list')







