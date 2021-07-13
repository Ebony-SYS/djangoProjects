from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Transacao
from .forms import TransacaoForm

'''
def home(request):
    """
    Função retorna data e hora por uma string html
    :param request: 
    :return: 
    """
    now = datetime.now()
    html = f'<html><body> Agora: {now}</body></html>'
    return HttpResponse(html)
'''


def home(request):
    """
    Função retorna como um response um template
    :param request:
    :return:
    """
    data = {}
    data['now'] = datetime.date().today()
    registros = ['t1', 't2', 't3']
    return render(request, 'contas/home.html', data, registros)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def novaTransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        # return listagem(request) Vai duplicar se atualizar
        return redirect('urlListagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    data = {}
    trasacao = Transacao.objects.get(pk=pk)  # pegando a transação do BD
    form = TransacaoForm(request.POST or None, instance=trasacao)

    if form.is_valid():
        form.save()
        return redirect('urlListagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('urlListagem')
