from django.shortcuts import render

# Create your views here.

def pesquisar(request):
    return render(request, 'produtos/pesquisa.html')


def exibir_resultados():
    pass