from django.db import models

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.titulo