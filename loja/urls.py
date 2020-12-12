from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.LojaTemplate.as_view(), name='homepage'),
    path('create/produto/', login_required(views.FileFieldFormView.as_view(), login_url='/'), name='register_produto_imagem'),
    path('produto/<int:id>', views.ProdutoView.as_view(), name='produto_page')
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 