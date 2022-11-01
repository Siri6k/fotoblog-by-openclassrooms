from django.conf import settings
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from . import forms

# Create your views here.

def login_page(request):
    form = forms.LoginForm()
    #message vide au depart
    message =''
    if request.method =='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # authentifier l'utilisateur
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                message = f'Bonjour,' \
                        f'{user.username}! Vous êtes connecté.'
                # connfigurez une redirectuion apres la connexion
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(request,
                  'authentication/login.html', context={'form': form,
                                                        'message': message}
                  )

def logout_user(request):
    logout(request)
    return redirect('login')
#vue d'inscription
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return  redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,
                  'authentication/signup.html', context={
            'form': form
        })
