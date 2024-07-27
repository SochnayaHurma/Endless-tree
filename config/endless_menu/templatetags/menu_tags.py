from django import template
from django.conf import settings

from endless_menu.models import MenuElements
from endless_menu.utils import build_tree

register = template.Library()


class MenuNode(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        query_set = MenuElements.objects.select_related('parent').filter(menu__name=self.menu_name)
        absolute_url = context.request.build_absolute_uri()
        engine = context.template.engine.get_template(
            f"{settings.MENU_TEMPLATES}{self.menu_name}.html"
        )
        return engine.render(template.Context(
            {'tree': build_tree(query_set, absolute_url)},
            autoescape=context.autoescape))


@register.tag
def draw_menu(parser, token):
    tag_name, menu_name = token.split_contents()
    return MenuNode(menu_name)
