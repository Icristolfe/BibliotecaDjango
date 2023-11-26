from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario']).nome
        return HttpResponse(f'<h1>Olá {usuario}</h1> <br> <a href="/auth/sair/">Sair</a>')
    else:
        return redirect('/auth/login/?status=2')
