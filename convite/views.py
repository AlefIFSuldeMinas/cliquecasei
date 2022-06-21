from http.client import HTTPResponse
from convite.models import ConviteCasamento
from django.shortcuts import render


def CadastroConvite(request):
    if request.method == "GET":
        return render(request, 'convite/convite_casamento.html')
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
        if request.user.is_authenticated:
            print(vars(convite))
        return render(request, 'convite/convite_casamento.html')

def Exemplo(request):
    
    return render(request, "convite/convite_casamento.html")


