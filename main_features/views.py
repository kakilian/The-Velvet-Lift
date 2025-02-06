from django.views.generic import TemplateView


def Index(request):
    return render(request, "main_features/index.html")
