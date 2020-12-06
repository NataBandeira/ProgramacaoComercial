from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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


class EnderecoForm(forms.Form):

    telefone_contato = forms.CharField(
        max_length=11,
        label='Telefone para contato:',
    )

    cep = forms.CharField(
        max_length=8,
        label='Cep:',
    )

    bairro = forms.CharField(
        max_length=120,
        label='Bairro:',
    )

    rua = forms.CharField(
        max_length=120,
        label='Rua:',
    )

    numero = forms.CharField(
        max_length=10,
        label='Número:',
    )

    informacao_adicional = forms.CharField(
        max_length=240,
        label='Informação adicional:',
    )

    class Meta:
        model = models.Endereco
        fields = ('telefone_contato', 'cep', 'bairro',
                  'rua', 'numero', 'informacao_adicional')

    def save(self, request):
        endereco = models.Endereco(
            telefone_contato=self.cleaned_data['telefone_contato'],
            cep=self.cleaned_data['cep'],
            bairro=self.cleaned_data['bairro'],
            rua=self.cleaned_data['rua'],
            numero=self.cleaned_data['numero'],
            informacao_adicional=self.cleaned_data['informacao_adicional'],
        )
        cliente = models.Cliente.objects.get(user=request.user.id)
        endereco.cliente = cliente
        endereco.save()
        return endereco


class UsuarioForm(forms.Form):

    username = forms.CharField(
        label='Nome:',
        widget=forms.TextInput(
            # attrs={'placeholder': 'Maria ..'}
        )
    )

    telefone = forms.CharField(
        max_length=11,
        label='Telefone:',
    )

    email = forms.EmailField(
        label='E-mail:',
    )

    password1 = forms.CharField(
        label='Senha:',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Confirme sua senha:',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(password1, password2)
        if password1 and password2 and password1 != password2:
            raise ValidationError("A senhas não correspondem")
        return password2

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        cliente = models.Cliente(
            telefone=self.cleaned_data['telefone'], user=user)
        cliente.save()
        return user
