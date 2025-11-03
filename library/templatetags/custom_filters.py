from django import template
from library.utils import is_bibliotecario, is_admin, is_cliente

register = template.Library()

register.filter('is_bibliotecario', is_bibliotecario)
register.filter('is_admin', is_admin)
register.filter('is_cliente', is_cliente)