from django import forms
from . import models


class ProdutoForm(forms.Form):
    produto_nome = forms.CharField(max_length=240, label='Nome do produto:')
    valor = forms.FloatField(label='Valor:')
    descricao = forms.CharField(label='Descrição:', max_length=480)
    imagem_produto = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = models.Produto
        fields = ['produto_nome', 'valor', 'descricao', 'imagem_produto']

    def save(self):
        produto = models.Produto.objects.create(
            produto_nome=self.cleaned_data['produto_nome'],
            valor=self.cleaned_data['valor'],
            descricao=self.cleaned_data['descricao'],
        )
        return produto