from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('login/', views.Authenticate.as_view(), name='logar_usuario'),
    path('logout/', views.logout_user, name='logout_usuario'),
    path('register/', views.register, name='cadastrar_usuario')
]