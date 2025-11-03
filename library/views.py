from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from .models import Livro, Emprestimo
from .forms import LivroForm, EmprestimoForm, EmprestimoStatusForm, RegisterForm
from .utils import is_bibliotecario, is_admin
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
    paginate_by = 10


    #Busca pelo título do livro
    def get_queryset(self):
        title = self.request.GET.get('title')

        if title:
            livros = Livro.objects.filter(title__icontains=title)
        else:
            livros = Livro.objects.all()
            
        return livros


class LivroCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Livro
    template_name = 'livros/livro_create.html'
    form_class = LivroForm
    success_url = reverse_lazy('livros_list')
    
    #Verifica se é bibliotecario ou admin
    def test_func(self):
        return is_bibliotecario(self.request.user) or is_admin(self.request.user)

class LivroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Livro
    template_name = 'livros/livro_update.html'
    form_class = LivroForm
    success_url = reverse_lazy('livros_list')

    #Verifica se é bibliotecario ou admin
    def test_func(self):
        return is_bibliotecario(self.request.user) or is_admin(self.request.user)

class LivroDetailView(DetailView):
    template_name = 'livros/livro_detail.html'
    model = Livro
    context_object_name = 'livro'

class LivroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Livro
    success_url = reverse_lazy('livros_list')

    #Verifica se é admin
    def test_func(self):
        return is_admin(self.request.user)


#Empréstimo
class EmprestimoListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'emprestimos/emprestimos_list.html'
    model = Emprestimo
    context_object_name = 'emprestimos'
    paginate_by = 10


    #Busca pelo status do empréstimo
    def get_queryset(self):
        status = self.request.GET.get('status')

        if status:
            emprestimos = Emprestimo.objects.filter(status__icontains=status) 
        else:
            emprestimos = Emprestimo.objects.all()
        
        return emprestimos
    
    #Verifica se é bibliotecario ou admin
    def test_func(self):
        return is_bibliotecario(self.request.user) or is_admin(self.request.user)


class EmprestimoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_create.html'
    form_class = EmprestimoForm
    success_url = reverse_lazy('emprestimos_list')

    def form_valid(self, form):
        emprestimo = form.save(commit=False)
        livro = emprestimo.book

        if livro.avaiable > 0:
            livro.emprestimo()
            emprestimo.save()
            return super().form_valid(form)
        else:
            form.add_error(None, 'Não há cópia disponível para empréstimo deste livro.')
            return super().form_invalid(form)
        
    #Verifica se é bibliotecario ou admin
    def test_func(self):
        return is_bibliotecario(self.request.user) or is_admin(self.request.user)


class EmprestimoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Emprestimo
    template_name = 'emprestimos/emprestimo_update.html'
    form_class = EmprestimoStatusForm
    success_url = reverse_lazy('emprestimos_list')

    def form_valid(self, form):
        emprestimo = form.save(commit=False)
        livro = emprestimo.book

        if emprestimo.status == 'returned':
            livro.devolver()

        emprestimo.save()
        return super().form_valid(form)

    #Verifica se é bibliotecario ou admin
    def test_func(self):
        return is_bibliotecario(self.request.user) or is_admin(self.request.user)

def solicitar_emprestimo(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    Emprestimo.objects.create(
        person=request.user,
        book=livro,
        status='pending'
    )
    return redirect('livros_list')

#Autenticação

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        cliente_group, created = Group.objects.get_or_create(name='Cliente')
        user.groups.add(cliente_group)

        return super().form_valid(form)




