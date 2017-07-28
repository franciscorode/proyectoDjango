from django.shortcuts import render

# Create your views here.

#hemos creado un método (def) llamado post_list que toma un request y hace un return de un método 
#render que renderizará (construirá) nuestra plantilla blog/post_list.html
def post_list(request):
    return render(request, 'aplicaciondeprueba/post_list.html', {})