from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UsuarioForm(forms.Form):

    username = forms.CharField(
        label='Nome usuario',
        widget=forms.TextInput(
            # attrs={'placeholder': 'Maria ..'}
        )
    )

    email = forms.EmailField(
        label='Email',
    )

    password1 = forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Enter password',
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
        return user

 # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password', 'password2')

    # def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.helper = FormHelper()
    #         self.helper.layout = Layout(
    #             Row(
    #                 Column('primeiro_nome', css_class='form-group col-md-6 mb-0'),
    #                 Column('sobrenome', css_class='form-group col-md-6 mb-0'),
    #                 css_class='form-row'
    #             ),
    #             Row(
    #                 Column('telefone', css_class='form-group col-md-6 mb-0'),
    #             ),
    #             Submit('submit', 'Sign in')
    #         )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save person'))
