from django.shortcuts import render
from .models import Produto


def pesquisar(request):
    return render(request, 'produtos/pesquisa.html')


def exibir_resultados(request):
    nome_produto = request.POST.get('produto')
    print(nome_produto)
    dados = { 'dados': Produto.objects.filter(name__icontains=nome_produto).order_by('price')}
    return render(request, 'produtos/resultado_pesquisa.html', dados)