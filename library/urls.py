from django.urls import path
from .views import IndexView, LivroListView, LivroCreateView, LivroUpdateView, LivroDetailView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('livros/', LivroListView.as_view(), name='livros_list'),
    path('livros/create/', LivroCreateView.as_view(), name='livro_create'),
    path('livros/update/<int:pk>/', LivroUpdateView.as_view(), name='livro_update'),
    path('livros/detail/<int:pk>/', LivroDetailView.as_view(), name='livro_detail'),
]