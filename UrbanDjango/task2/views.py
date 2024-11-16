from django.shortcuts import render
from django.views.generic import TemplateView

def functemplate(request):
    return render(request,'func_template.html')

class ClassTemplate(TemplateView):
    template_name = 'class_template.html'
# Create your views here.
