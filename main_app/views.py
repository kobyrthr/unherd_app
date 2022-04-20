from pipes import Template
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from .models import Event

# Create your views here.
class Index(TemplateView):
    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        return context



