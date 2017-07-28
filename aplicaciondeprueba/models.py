from django.db import models
from django.utils import timezone

#Modelo/Clase Post
#models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
class Post(models.Model):
#propiedades/atributos de la clase
	
	#models.CharField - así es como defines un texto con un número limitado de caracteres.
    #models.TextField - esto es para textos largos sin un límite. Será ideal para el contenido de un post, ¿verdad?
    #models.DateTimeField - esto es fecha y hora.
    #modelos.ForeignKey - este es un vínculo con otro modelo.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
