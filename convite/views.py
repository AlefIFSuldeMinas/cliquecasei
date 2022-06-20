from convite.models import ConviteCasamento
from django.shortcuts import render
from django.http import HttpResponse


def CadastroConvite(request):
    context = {}
    if request.method == "POST":
        form = ConviteCasamento(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("geeks_field")
            obj = ConviteCasamento.objects.create(
                                 title = name,
                                 img = img
                                 )
            obj.save()
            print(obj)
    else:
        form = ConviteCasamento()
    context['form']= form
    return render(request, "convite/cadastro_convite.html", context)

def Exemplo(request):
    return render(request, "convite/convite_casamento.html")
