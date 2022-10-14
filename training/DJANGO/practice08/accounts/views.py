from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request, data=request.POST)
        
        if form.is_vaild():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()

    context = {
        "form" : form,
    }
    
    return render(request, "accounts/signup.html", context)