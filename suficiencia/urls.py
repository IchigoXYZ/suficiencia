"""
URL configuration for suficiencia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recursos_humanos_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.crearTrabajador),
    path('eliminar/', views.eliminar_trabajador),
    path('lista/', views.listar_trabajadores),
    path('login/', views.loguear),
    path('crear_usuario/', views.crear_usuario),
    
]
