from collections import defaultdict

from django import template

from endless_menu.models import MenuElements
from endless_menu.utils import check_active

register = template.Library()


@register.inclusion_tag(filename='navigations/menu.html')
def draw_menu(request, menu_name):
    tree, links = defaultdict(dict), defaultdict(dict)
    qs = MenuElements.objects.select_related('parent').filter(menu__name=menu_name)
    for item in qs:
        link = links[item]
        if item.parent:
            links[item.parent][item] = link
        else:
            tree[item] = link
    checked_tree, _ = check_active(request.build_absolute_uri(), tree)
    return {'tree': checked_tree}
