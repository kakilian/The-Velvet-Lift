from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "main_features/index.html"
