from django.shortcuts import render
from sistema.models import Medico

def listarMedicos(request):
    medicos = Medico.objects.all()  # Variável medicos está guardando todos os objetos da tabela Medico.

    context = { # Declaração de um dict que possui a chave medicos e o valor medicos(variável criada acima).
        'medicos': medicos,
    }
    
    return render(
        request,
        'medico/listar.html',
        context,
    )