from django.shortcuts import render

# Aqui fica a primeira view
def index(request):
    return render(
        request,
        'global/base.html'
    )


# REQUEST - RESPONSE - RENDER

# Testando
def teste(request):
    return render(
        request,
        'global/teste.html'
    )

def seunome(request):
    return render(
        request,
        'global/seunome.html'
    )