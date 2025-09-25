from django.urls import path
from .views import IndexView, LivroListView 
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('livros/', LivroListView.as_view(), name='livros_list'),

]