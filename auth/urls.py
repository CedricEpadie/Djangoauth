from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
]