from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home' ),
    path('ver_livros/<int:id>', views.ver_livros, name='ver_livros'),
    path('cadastrar_livro', views.cadastrar_livro, name='cadastrar_livro'),
    path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro')
  ]