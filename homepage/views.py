from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View
from dashboard.forms import UsuarioForm

def login_page(request):
    template = loader.get_template('homepage/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def logout_user(request):
    logout(request)
    return redirect('/')


def register(request):
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('/home/')
                
            else:
                print("ERROR")
                form = UsuarioForm(request.POST)
                return render(request, 'homepage/cadastrar_usuario.html', {'form': form})
            
        else:
            form = UsuarioForm()
            return render(request, 'homepage/cadastrar_usuario.html', {'form': form})

class Authenticate(View):

    def post(self, request):
        print("Entrou")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'homepage/login.html', {"errors": "Combinação de login e senha errada"})
