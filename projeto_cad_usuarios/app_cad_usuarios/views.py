from django.shortcuts import render
from .models import Usuario

def home(request):
     return render(request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        # Salvar os dados da tela para o DB.
        novo_usuario = Usuario()
        novo_usuario.nome_usuario = request.POST.get('nome')
        novo_usuario.idade_usuario = request.POST.get('idade')
        novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
