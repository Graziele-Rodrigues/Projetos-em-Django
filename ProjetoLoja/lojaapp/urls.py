from lojaapp.views import *
from django.urls import path 

app_name = "lojaapp"
urlpatterns =  [
    path("", HomeView.as_view(), name="home"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("todos-produtos/", TodosProdutosView.as_view(), name="todos-produtos"),
    path("produto/<slug:slug>/", DetalheProdutoView.as_view(), name="detalhe-produto"),
    path("addCarrinho-<int:id>/", AddCarrinho.as_view(), name="add-carrinho"),
    path("meuCarrinho/", MeuCarrinho.as_view(), name="meuCarrinho"),
]