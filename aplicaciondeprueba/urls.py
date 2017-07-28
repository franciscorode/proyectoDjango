#Aquí solo estamos importando los métodos de Django y todas nuestras views del blog
from django.conf.urls import include, url
from . import views

#agregamos patrones de urls y las asignamos a una vista
urlpatterns = [
    url(r'^$', views.post_list),
]
