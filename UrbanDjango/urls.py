"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tempfile import template

from django.contrib import admin
from django.urls import path
#from task2.views import func_template, TemplateClass
from task3.views import cart, games, platform

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', func_template),
    # path('class_template/', TemplateClass.as_view())
    path('platform/', platform),
    path('games/', games),
    path('cart/', cart),
]