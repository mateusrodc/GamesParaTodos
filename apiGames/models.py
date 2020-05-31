from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    apelido = models.CharField(max_length=200)
    

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        
        return "({})".format(self.apelido)

class Autor(models.Model):
    nome_autor = models.CharField(max_length=250,null=False,blank=False)

    class Meta:
        db_table = 'autor'

    def __str__(self):
        
        return "({})".format(self.nome_autor)

class Livro(models.Model):
    titulo = models.CharField(max_length=250,null=False,blank=False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    pontuacao_maxima = models.IntegerField()

    class Meta:
        db_table = 'livro'
        ordering = ['titulo']

    def __str__(self):
        
        return "({})".format(self.titulo)