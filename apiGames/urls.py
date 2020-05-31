from rest_framework import routers


router = routers.DefaultRouter()
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from apiGames.views import *



urlpatterns = [
    #Usuarios
    path('usuarios/', UsuarioList.as_view()),
    path('usuarioID/<int:pk>', UsuarioID.as_view()),
    path('listaUsuarios/', UsuarioListAll.as_view()),
    path('usuarios/<int:pk>', UsuarioDetalhes.as_view()),
    #Autor
    path('autor/', AutorList.as_view()),
    path('autorID/<int:pk>', AutorID.as_view()),
    path('listaAutor/', AutorListAll.as_view()),
    path('autor/<int:pk>', AutorDetalhes.as_view()),
    #Livro
    path('livro/',LivroList.as_view()),
    path('livro/<int:pk>',LivroDetalhes.as_view())


]