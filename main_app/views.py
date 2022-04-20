from pipes import Template
from pyexpat import model
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Event

# Create your views here.
class Index(TemplateView):
    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        title = self.request.GET.get("title")

        if title != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["events"] = Event.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["events"] = Event.objects.all()
            context["header"] = "Upcoming Events"
        return context

class EventDetail(DetailView):
    model = Event
    template_name='event_detail.html'

