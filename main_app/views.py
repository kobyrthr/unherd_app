from pipes import Template
import profile
from pyexpat import model
from turtle import rt
from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Event, RSVP, Profile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse_lazy
from .forms import RSVPForm


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

class ProfileView(TemplateView):
    model = Profile
    template_name= 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.all()
        context["rsvps"] = RSVP.objects.filter(user=self.request.user)
        return context

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
    

class EventUpdate(UpdateView):
    model = Event
    fields = ['img_2','img','title','description','genres']
    template_name = 'event_update.html'
    success_url = '/'


class EventDelete(DeleteView):
    model = Event
    fields = '__all__'
    template_name="event_delete.html"
    success_url = "/"

class RSVP_Post(CreateView):
    form_class = RSVPForm
    template_name = 'rsvp_post.html'
    success_url = '/'
    
    def get_initial(self):
        event = get_object_or_404(Event, id=self.kwargs.get('<int:pk>'))
        return {
            'event':event,
        }