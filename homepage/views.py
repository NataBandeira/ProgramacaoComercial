from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from .forms import *
from .models import *
from django.contrib.messages import get_messages

# AUTENTIFICACAO


def login_page(request):
    template = loader.get_template('homepage/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def logout_user(request):
    logout(request)
    return redirect('/')


class Authenticate(View):

    def post(self, request):
        print("Entrou")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/loja')
        else:
            return render(request, 'homepage/login.html', {"errors": "Combinação de login e senha errada"})

# USUARIO


class UsuarioUpdateView(LoginRequiredMixin, View):
    template_name = 'homepage/cliente_page.html'
    success_url = '/dash'

    def get(self, request, **kwargs):
        id = self.kwargs.get('id')
        cliente = get_object_or_404(Cliente, user=id)
        form_u = UserForm(instance=self.request.user)
        form_c = ClienteForm(instance=cliente)
        context = {
            'form_u': form_u,
            'form_c': form_c,
            'user': self.request.user,
            'cliente': cliente,
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        id = self.kwargs.get('id')
        cliente = get_object_or_404(Cliente, user=id)
        form_u = UserForm(request.POST, instance=self.request.user)
        form_c = ClienteForm(request.POST, instance=cliente)

        if form_u.is_valid() and form_c.is_valid():
            user = form_u.save()
            cliente = form_c.save()
            return HttpResponseRedirect('/loja')
        else:
            context = {
                'form_u': form_u,
                'form_c': form_c,
                'user': self.request.user,
                'cliente': cliente,
            }
            return render(request, self.template_name, context)

class UsuarioFormView(View):
    
    def get(self, request):
        context = {
            'form_u':  UserForm(),
            'form_c': ClienteForm(),
        }
        return render(request, 'homepage/cliente_page.html', context)

    def post(self, request):

        form_u = UserForm(request.POST)
        form_c = ClienteForm(request.POST)

        if form_u.is_valid() and form_c.is_valid():
            user = form_u.save()
            cliente = form_c.save(commit=False)
            cliente.user = user
            cliente.save()
            return redirect('/')
        else:
            context = {
                'form_u': form_u,
                'form_c': form_c, 
            }
            return render(request, 'homepage/cliente_page.html', context)


# ENDERECO


class EnderecoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EnderecoForm
    template_name = 'dashboard/dashboard_usuario_create.html'
    success_url = '/dash'
    model = Endereco


class EnderecoFormView(LoginRequiredMixin, FormView):
    form_class = EnderecoForm
    template_name = 'homepage/register_endereco.html'
    success_url = '/home/'

    def form_valid(self, form) -> HttpResponse:
        endereco = form.save(self.request)
        if endereco:
            return redirect('/home/')
        return self.form_valid(form)
