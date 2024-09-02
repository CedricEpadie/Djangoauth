from django.contrib import admin
from django.urls import path, include

from auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.acceuil),
    path('auth/', include('auth.urls')),
]
