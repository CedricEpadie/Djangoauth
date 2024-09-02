from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth:profil')
    else:
        form = UserCreationForm()
        
    return render(request, 'auth/inscription.html', {'form' : form})

def connexion(request):
    return render(request, 'auth/connexion.html')

def deconnexion(request):
    pass

def acceuil(request):
    return render(request, 'auth/acceuil.html')

def profil(request):
    return render(request, 'auth/profil.html')