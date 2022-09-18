from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Contato
from django.views import generic
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 2
    context_object_name = 'contatos'

    def get_queryset(self, **kwargs):
        termo = self.request.GET.get('termo')
        if termo is not None:
            if not termo:
                messages.add_message(
                    self.request,
                    messages.ERROR,
                    'Essa nao pode estar em branco',
                )
            else:
                messages.add_message(
                    self.request,
                    messages.SUCCESS,
                    'Enviado',
                )

        if termo:
            campos = Concat('nome', Value(' '), 'sobrenome')
            return Contato.objetos.annotate(nome_completo=campos).filter(
                Q(nome_completo__icontains=termo) | Q(id__icontains=termo)
                )

        return Contato.objetos.order_by('-id').filter(mostrar=True)


class Ver_ContatoView(generic.ListView):
    template_name = 'ver_contato.html'
    context_object_name = 'contato'

    def get_queryset(self, **kwargs):
        if self.kwargs:
            contato = get_object_or_404(Contato, slug=self.kwargs['slug'])
            if not contato.mostrar:
                raise Http404
            return contato
