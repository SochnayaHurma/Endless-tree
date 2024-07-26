from django.contrib import admin

from .models import MenuElements


class MainMenuInline(admin.TabularInline):
    model = MenuElements
    fk_name = 'parent'
    exclude = ['menu']


@admin.register(MenuElements)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    prepopulated_fields = {'named_url': ('name',)}
    inlines = [MainMenuInline]
