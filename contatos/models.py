from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=150, blank=False, null= False)
    sobrenome = models.CharField(max_length=150, blank=True)
    telefone = models.IntegerField(blank=False, null=False)
    email = models.EmailField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=400, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    slug = models.SlugField(null=False)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')
    objetos = models.Manager()

    def __str__(self):
        return self.nome
