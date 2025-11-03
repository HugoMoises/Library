from django.contrib.auth.models import User

#verificar se é bibliotecário
def is_bibliotecario(user):
    return user.groups.filter(name='Bibliotecário').exists()

#verificar se é administrador
def is_admin(user):
    return user.groups.filter(name='Administrador').exists()

def is_cliente(user):
    return user.groups.filter(name='Cliente').exists()

def is_admin_or_bibliotecario(user):
    return is_admin(user) or is_bibliotecario(user)