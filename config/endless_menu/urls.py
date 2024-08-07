from django.urls import path, re_path
from django.views.generic import TemplateView

app_name = 'menu'

urlpatterns = [
    re_path(r"(.+)?", TemplateView.as_view(template_name='index.html'))
]
