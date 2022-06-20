from django import forms

class ConviteCasamento(forms.Form):
    Capa = forms.ImageField()
    NomeNoivos = forms.CharField(max_length=100)
    DataCasamento = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    GaleriaId = forms.IntegerField()
    Descricao = forms.CharField(widget=forms.Textarea)
    Onde = forms.CharField(widget=forms.Textarea)
    ListaPresentes = forms.CharField(max_length=100)

