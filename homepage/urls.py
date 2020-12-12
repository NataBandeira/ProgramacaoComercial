from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login/', views.Authenticate.as_view(), name='logar_usuario'),
    path('logout/', views.logout_user, name='logout_usuario'),
    path('cliente/<int:id>', views.UsuarioUpdateView.as_view(), name='atualizar_usuario'),
    path('create/cliente', views.UsuarioFormView.as_view(), name='cadastrar_usuario'),
    path('create/endereco/', views.EnderecoFormView.as_view(), name='register_endereco'),
    path('update/endereco/', views.EnderecoUpdateView.as_view(), name='update_endereco'),
]