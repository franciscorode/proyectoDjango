#Aquí solo estamos importando los métodos de Django y todas nuestras views del blog
from django.conf.urls import include, url
from . import views

#agregamos patrones de urls y las asignamos a una vista
urlpatterns = [
    url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]



#comienza con ^ otra vez, "el principio".

#post/ sólo significa que después del comienzo, la dirección URL debe contener la palabra
# post y /. Hasta ahora, bien.
 
#(?P<pk>[0-9]+) - esta parte es más complicada. Significa que Django llevará todo lo que coloques 
#aquí y lo transferirá a una vista como una variable llamada pk. [0-9] también nos dice que sólo 
#puede ser un número, no una letra (todo debería estar entre 0 y 9). + significa que tiene que 
#haber uno o más dígitos. Entonces algo como http://127.0.0.1:8000/post// no es válido, 
#pero http://127.0.0.1:8000/post/1234567890/ es perfectamente aceptable!

#/ - entonces necesitamos / de nuevo
#$ - ¡"el final"!
