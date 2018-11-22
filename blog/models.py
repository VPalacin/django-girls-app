from django.db import models
from django.utils import timezone


class Post(models.Model): #objeto Post que a su vez es un modelo de la clase Model, se guarda en la BD
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT) #relación con otro modelo
    title = models.CharField(max_length=200) #nº de caracteres limitados
    text = models.TextField() #texto largo sin limite
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #métodos: guiones bajos y minúscula: nombre_de_mi_metodo
    def publish(self): #self funciona como un puntero al objeto
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #devuelve un objeto __str__() con el título del post
