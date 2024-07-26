from django.contrib import admin

from .models import MenuElements, MenuList


class MainMenuInline(admin.TabularInline):
    model = MenuElements
    fk_name = 'parent'
    exclude = ['menu']


@admin.register(MenuElements)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    inlines = [MainMenuInline]

    def get_form(self, request, *args, **kwargs):
        form = super().get_form(request, *args, **kwargs)
        form.base_fields['abs_url'].initial = request.build_absolute_uri('/')
        return form


admin.site.register(MenuList)
