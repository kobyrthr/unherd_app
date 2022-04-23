from pipes import Template
from pyexpat import model
from turtle import rt
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from requests import request
from .models import Event
from .models import RSVP

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,'signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect('/')
                    else:
                        print('The account has been disabled.')
                        return render(request, 'login.html', {'form':form})
            else:
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form':form})
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})
                

class Index(TemplateView):
    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        title = self.request.GET.get("title")

        if title != None:
            context["events"] = Event.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["events"] = Event.objects.all()
            context["header"] = "Upcoming Events"
        return context

class Event_Create(CreateView):
    model = Event
    fields = ['img_2','img','title','description','genres']
    template_name = 'event_create.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class EventDetail(DetailView):
    model = Event
    template_name='event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        context["rsvps"] = RSVP.objects.filter(event = self.get_object())
    #     # User = get_user_model()
    #     # context["user"] = User.objects.all()
        return context
    

