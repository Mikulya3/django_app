from mainapp.views import draw_menu
from django import template

register = template.Library()
register.simple_tag(draw_menu)
