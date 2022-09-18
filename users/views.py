from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormContato


class AccountsView(generic.TemplateView):
    template_name = 'accounts.html'


def login_view(request):
    if request.method != 'POST':
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = authenticate(username=usuario,
                        password=senha)
    if not user:
        messages.error(request, 'Usuario ou senha invalida.')
        return render(request, 'login.html')
    else:
        messages.success(request, 'Logado')
        login(request, user)
        return HttpResponseRedirect(reverse('users:dashboard'))


def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse('users:accounts'))


def register(request):
    """Faz o cadastro de um novo usuario."""
    if request.method != 'POST':
        # Exibe o formulario de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulario preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuario e o redireciona para a pagina inicial
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)
            messages.success(request, 'Cadastro enviado')
            return HttpResponseRedirect(reverse('users:login'))
    context = {'form': form}
    return render(request, 'cadastro.html', context)


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
    else:
        form = FormContato(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, f'Contato {request.POST.get("nome")} Salvo')
            form.save()
            return HttpResponseRedirect(reverse('users:dashboard'))

        else:
            messages.error(request, 'Erro ao enviar')
            form = FormContato(request.POST, request.FILES)
            context = {'form': form}
            return render(request, 'dashboard.html', context)

    context = {'form': form}
    return render(request, 'dashboard.html', context)