from django.urls import path
from . import views

urlpatterns = [
    path('', views.PedidosView.as_view(), name='pedidos_page')
]