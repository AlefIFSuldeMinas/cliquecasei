from http.client import HTTPResponse
from convite.models import ConviteCasamento, Convidados
from django.shortcuts import render
from django.http import HttpResponse



def CadastroConvite(request):
    if request.method == "GET":
        return render(request, 'convite/cadastro_convite.html')
    else:
        NomeNoiva = request.POST.get('NomeNoiva')
        NomeNoivo = request.POST.get('NomeNoivo')
        DataCasamento = request.POST.get('DataCasamento')
        Capa = request.POST.get('Capa')
        FotoCasal = request.POST.get('FotoCasal')
        Descricao = request.POST.get('Descricao')
        Endereco = request.POST.get('Endereco')
        Cidade = request.POST.get('Cidade')
        Estado = request.POST.get('Estado')
        Cep = request.POST.get('Cep')
        ListaPresentes = request.POST.get('ListaPresentes')
        IdUsuario = request.user.id
        convite = ConviteCasamento.objects.create(
            NomeNoiva = NomeNoiva,
            NomeNoivo = NomeNoivo,
            DataCasamento = DataCasamento,
            Capa = Capa,
            FotoCasal = FotoCasal,
            Descricao = Descricao,
            Endereco = Endereco,
            Cidade = Cidade,
            Estado = Estado,
            Cep = Cep,
            ListaPresentes = ListaPresentes,
            IdUsuario = IdUsuario
        )
        convite.save()
        return ConviteCasamentoVM(request, int(ConviteCasamento.objects.count()))

def ConviteCasamentoVM(request, codigoId):
    convites = ConviteCasamento.objects.order_by('id')[int(codigoId)]
    contexto = {
      'convites': convites
    }
    return render(request, "convite/convite_casamento.html", contexto)

def CadastrarConvidado(request):
    NomeConvidado =  request.POST.get('NomeConvidado')
    Acompanhantes =  request.POST.get('Acompanhantes')
    TelefoneConvidado = request.POST.get('TelefoneConvidado')
    Observacoes = request.POST.get('Observacoes')
    IdCasal = request.POST.get('IdCasal')

    convidados = Convidados.objects.create(
            NomeConvidado = NomeConvidado,
            Acompanhantes = Acompanhantes,
            TelefoneConvidado = TelefoneConvidado,
            Observacoes = Observacoes,
            IdCasal = IdCasal
        )
    convidados.save()
    return HttpResponse('Presença confirmada!')









