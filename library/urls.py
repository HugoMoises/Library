from django.urls import path
from .views import IndexView, LivroListView, LivroCreateView, LivroUpdateView, LivroDetailView, LivroDeleteView, EmprestimoCreateView, EmprestimoListView, EmprestimoUpdateView, RegisterView, solicitar_emprestimo
#Autenticação
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    #Livros
    path('livros/', LivroListView.as_view(), name='livros_list'),
    path('livros/create/', LivroCreateView.as_view(), name='livro_create'),
    path('livros/update/<int:pk>/', LivroUpdateView.as_view(), name='livro_update'),
    path('livros/detail/<int:pk>/', LivroDetailView.as_view(), name='livro_detail'),
    path('livros/delete/<int:pk>', LivroDeleteView.as_view(), name='livro_delete'),

    #Empréstimo
    path('emprestimos', EmprestimoListView.as_view(), name='emprestimos_list'),
    path('emprestimos/create/', EmprestimoCreateView.as_view(), name='emprestimo_create'),
    path('emprestimos/update/<int:pk>/', EmprestimoUpdateView.as_view(), name='emprestimo_update'),
    path('solicitar_emprestimo/<int:pk>/', solicitar_emprestimo, name='solicitar_emprestimo'),

    #Autenticação
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]