from django.http import HttpResponse
from django.template import loader
from catalog.models import Post

# Create your views here.
def hello_world(request):
    posts_list = Post.objects.all()
    template = loader.get_template('hello_world.html')
    context = {
        'posts_list': posts_list,
    }
    return HttpResponse(template.render(context, request))
