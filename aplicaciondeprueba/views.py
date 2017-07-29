from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

#hemos creado un método (def) llamado post_list que toma un request y hace un return de un método 
#render que renderizará (construirá) nuestra plantilla blog/post_list.html
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'aplicaciondeprueba/post_list.html', {'posts': posts})