from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_example(request):
    return render(request, 'func_template.html')


class class_example(TemplateView):
    template_name = 'class_template.html'