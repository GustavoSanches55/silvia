from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_route, name='home'),
    path('aluno', views.aluno, name='aluno'),

]