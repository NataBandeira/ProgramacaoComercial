from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from . import forms
from . import models
from django.views.generic.edit import FormView


class FileFieldFormView(FormView):
    form_class = forms.ProdutoForm
    template_name = 'dashboard/register_produto.html'
    success_url = '/home/'

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('imagem_produto')
        if form.is_valid():
            produto = form.save()
            for f in files:
                imagem = models.ImagemProduto.objects.create(
                    imagem_produto=f,
                    produto=produto
                )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class EnderecoFormView(FormView):
    form_class = forms.EnderecoForm
    template_name = 'dashboard/register_endereco.html'
    success_url = '/home/'

    def form_valid(self, form) -> HttpResponse:
        endereco = form.save(self.request)
        if endereco:
            return redirect('/home/')
        return self.form_valid(form)


class DashHomeView(View):
    def get(self, request):
        print("Entrou aqui")
        return render(request, 'dashboard/homepage.html', {})
