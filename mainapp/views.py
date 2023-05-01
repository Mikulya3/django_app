from django.shortcuts import render

from django import template
from django.urls import reverse

from mainapp.models import Menu

register = template.Library()
@register.simple_tag()
def draw_menu(menu_name):
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')
    return render_menu(menu_items)
@register.simple_tag()
def render_menu(menu_items):
    result = '<ul>'
    for item in menu_items:
        is_active = check_active(item.url)
        if item.parent_id is None:
            result += '<li class="{}">'.format('active' if is_active else '')
        else:
            result += '<li>'
        result += '<a href="{}" class="{}">{}</a>'.format(item.url, 'active' if is_active else '', item.name)
        if item.children.exists():
            result += render_menu(item.children.all())
        result += '</li>'
    result += '</ul>'
    return result
@register.simple_tag()
def check_active(url):
    current_url = reverse('current_url_name')
    return current_url == url

