from django import template

from endless_menu.models import MenuElements
from endless_menu.utils import build_tree

register = template.Library()


@register.inclusion_tag(filename='navigations/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    query_set = MenuElements.objects.select_related('parent').filter(menu__name=menu_name)
    absolute_url = context.request.build_absolute_uri()
    return {'tree': build_tree(query_set, absolute_url)}
