from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, View
from .forms import *
from .models import *
from django.views.generic.edit import FormView


class LojaTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'loja/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(*args, **kwargs)
        data = []
        produtos = Produto.objects.all()
        for produto in produtos:
            data.append({
                'produto': produto,
                'imagem': ImagemProduto.objects.filter(produto_id=produto.id)[0]
            })
        context['produtos'] = data
        context['user'] = self.request.user
        return context


class FileFieldFormView(FormView):
    form_class = ProdutoForm
    template_name = 'loja/register_produto.html'
    success_url = '/loja/'

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('imagem_produto')
        if form.is_valid():
            produto = form.save()
            for f in files:
                imagem = ImagemProduto.objects.create(
                    imagem_produto=f,
                    produto=produto
                )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DashHomeView(View):
    def get(self, request):
        print("Entrou aqui")
        return render(request, 'loja/homepage.html', {})
