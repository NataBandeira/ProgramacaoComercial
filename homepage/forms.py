from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    username = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            # attrs={'placeholder': 'Maria ..'}
        )
    )

    email = forms.EmailField(
        label='E-mail',
    )


    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2', ]

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("A senhas não correspondem")
    #     return password2

    # def save(self):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password1']
    #     )
    #     return user


class ClienteForm(forms.ModelForm):

    telefone = forms.CharField(
        max_length=11,
        label='Telefone:',
    )

    class Meta:
        model = Cliente
        fields = ['telefone']

    # def save(self, user):
    #     cliente = Cliente(
    #         telefone=self.cleaned_data['telefone'],
    #         user=user
    #     )
    #     cliente.save()
    #     return cliente


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
        model = Endereco
        fields = ('telefone_contato', 'cep', 'bairro',
                  'rua', 'numero', 'informacao_adicional')

    def save(self, request):
        endereco = Endereco(
            telefone_contato=self.cleaned_data['telefone_contato'],
            cep=self.cleaned_data['cep'],
            bairro=self.cleaned_data['bairro'],
            rua=self.cleaned_data['rua'],
            numero=self.cleaned_data['numero'],
            informacao_adicional=self.cleaned_data['informacao_adicional'],
        )
        endereco.user = request.user
        endereco.save()
        return endereco


# class UsuarioForm(forms.ModelForm):

#     username = forms.CharField(
#         label='Nome:',
#         widget=forms.TextInput(
#             # attrs={'placeholder': 'Maria ..'}
#         )
#     )

#     telefone = forms.CharField(
#         max_length=11,
#         label='Telefone:',
#     )

#     email = forms.EmailField(
#         label='E-mail:',
#     )

#     password1 = forms.CharField(
#         label='Senha:',
#         widget=forms.PasswordInput
#     )

#     password2 = forms.CharField(
#         label='Confirme sua senha:',
#         widget=forms.PasswordInput
#     )

#     class Meta:
#         model = User
#         fields = ['username','email','telefone']

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         print(password1, password2)
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("A senhas não correspondem")
#         return password2

#     def save(self):
#         user = User.objects.create_user(
#             self.cleaned_data['username'],
#             self.cleaned_data['email'],
#             self.cleaned_data['password1']
#         )
#         cliente = models.Cliente(
#             telefone=self.cleaned_data['telefone'],
#             user=user
#         )
#         cliente.save()
#         return user
