from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/endereco/', views.register_endereco, name='register_endereco'),
    path('register/produtoimagem/', login_required(views.FileFieldView.as_view(), login_url='/'), name='register_produto_imagem')
]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 