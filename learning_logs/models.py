from django.db import models

# Create your models here.

"""Um assunto sobre o qual o usuario esta aprendendo"""
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    #Devolve uma representação em string do modelo.
    def __str__(self):
        return self.text