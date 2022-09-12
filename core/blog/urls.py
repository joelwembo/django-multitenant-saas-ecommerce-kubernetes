from django.urls import path
from django.views.generic import TemplateView

# Url and addressing

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]
