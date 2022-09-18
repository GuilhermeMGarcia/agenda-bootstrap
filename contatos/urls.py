from django.urls import path
from .views import IndexView, Ver_ContatoView

app_name = 'contatos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('busca/', IndexView.as_view(), name='busca'),
    path('contato/<slug:slug>', Ver_ContatoView.as_view(), name='ver_contato'),
]