from django.shortcuts import render

def inscription(request):
    return render(request, 'auth/inscription.html')

def connexion(request):
    return render(request, 'auth/connexion.html')

def deconnexion(request):
    pass

def acceuil(request):
    return render(request, 'auth/acceuil.html')

def profil(request):
    return render(request, 'auth/profil.html')