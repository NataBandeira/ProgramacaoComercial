from django.views.generic.base import View
from pedido.models import Pedido
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render


class PedidosView(LoginRequiredMixin, View):
    template_name = 'pedido/pedidos_page.html'

    def get(self, request):
        pedidos = Pedido.objects.filter(user=request.user)        
        context = {
            'user': self.request.user,
            'pedidos': pedidos
        }
        return render(request, self.template_name, context)



