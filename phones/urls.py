"""
URL configuration for phones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path , include

import moto,vivo,oppo,redme

from moto.views import *
from vivo.views import *
from oppo.views import *
from redme.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moto/',include('moto.urls')),
    path('ultra/',ultra,name='ultra'),
    path('vivo/',include('vivo.urls')),
    path('Y200_5G/',Y200_5G,name='Y200_5G'),
    path('oppo/',include('oppo.urls')),
    path('A_38/',A_38,name='A_38'),
    path('redme/',include('redme.urls')),
    path('Global/',Global,name='Global'),     
]
