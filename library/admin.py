from django.contrib import admin
from .models import Pessoa, Livro, Emprestimo


admin.site.register(Pessoa)
admin.site.register(Livro)
admin.site.register(Emprestimo)