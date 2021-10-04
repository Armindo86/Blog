from django.contrib.auth.models import User
from django.db import models


#Postes para blog
class Post(models.Model):
    title = models.CharField(max_length=255) #cria campos varchar(TITLO DE POSTAGEM)
    slug = models.SlugField(max_length=255, unique=True) #www.meusite.com/blog/introdução
    author = models.ForeignKey(User, on_delete=models.CASCADE) #AUTOR DE POSTAGEM COM O ID

