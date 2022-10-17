from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    users = get_user_model().objects.all()

    context = {
        'users' : users
    }

    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:login')

    else:
        form = CustomUserCreationForm()

    context = {
        "form" : form,
    }
    
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            return redirect("accounts:index")
    
    else:
        form = AuthenticationForm()

    context = {
        "form" : form
    }

    return render(request, "accounts/login.html", context)

def detail(request, pk):
    return render(request, 'accounts/detail.html')

def update(request, pk):
    return render(request, 'accounts/update.html')

def delete(request, pk):
    pass