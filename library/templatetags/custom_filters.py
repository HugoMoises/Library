from django import template

register = template.Library()

@register.filter
def is_bibliotecario(user):
    return user.groups.filter(name='Bibliotecário').exists()

@register.filter
def is_admin(user):
    return user.groups.filter(name='Administrador').exists()