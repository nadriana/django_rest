#para simplificar donde estan todos los django project urls are
# esto es diferente al archivo urls.py que está en el root del projecto de django (cfehome/urls.py)

from django.urls import path

from . import views #equivalente a from .views import api_home


urlpatterns = [
    path('', views.api_home) #localhost:800/api/



]