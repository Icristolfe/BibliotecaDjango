from django.shortcuts import redirect,render
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro
from django.http import HttpResponse


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']

        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

        return render(request, 'home.html', {'livros': livros,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form':form})

    else:
        return redirect('/auth/login/?status=2')


def ver_livros(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.get(id=id)
        categoria_livro = Categoria.objects.filter(usuario_id=request.session.get(
            'usuario'))  # Filtrando categoria de acordo com o usuario que está logado
        emprestimos = Emprestimo.objects.filter(livro=livros)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)


        if request.session.get('usuario') == livros.usuario.id:
            return render(request, 'ver_livro.html', {'livro': livros, 'categoria_livro': categoria_livro,
                                                      'emprestimos': emprestimos,
                                                      'usuario_logado': request.session.get('usuario'),
                                                        'form':form,
                                                        'id_livro': id})
        else:
            return HttpResponse("Esse livro não é seu")
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == "POST":
        form = CadastroLivro(request.POST)
    
    if form.is_valid():
        form.save()
        return  redirect('/livro/home')
    else:
      return  HttpResponse('Dados invalidos')
    


def excluir_livro(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()

    return redirect('/livro/home')
