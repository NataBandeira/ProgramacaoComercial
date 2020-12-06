from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin



class FileFieldView(FormView):
    form_class = forms.ProdutoForm
    template_name = 'dashboard/register_produto.html'
    success_url = '/home/'

    @login_required(login_url='/')
    def post(self, request, *args, **kwargs):
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


@login_required(login_url='/')
def register_endereco(request):
    form = forms.EnderecoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            endereco = form.save(request)
            if endereco:
                return redirect('/home/')
        else:
            print("ERROR")
            form = forms.EnderecoForm(request.POST)
            return render(request, 'dashboard/register_endereco.html', {'form': form})
    else:
        form = forms.EnderecoForm()
        return render(request, 'dashboard/register_endereco.html', {'form': form})


@login_required(login_url='/')
def homepage(request):
    template = loader.get_template('dashboard/homepage.html')
    context = {}
    return HttpResponse(template.render(context, request))
