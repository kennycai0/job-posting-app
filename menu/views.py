from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


def menu(request):
    return render(request, "menu/menu.html")


def home(request):
    return render(request, "menu/home.html")


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/login.html'
