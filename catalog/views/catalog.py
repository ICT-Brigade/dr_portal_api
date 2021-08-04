from django.http import HttpResponse
from django.template import loader
from catalog.models import Post
from main.settings import STATIC_URL


# Create your views here.
def list(request):
    posts_list = Post.objects.all()
    template = loader.get_template('../templates/catalog_list.html')
    context = {
        'posts_list': posts_list,
        'static_url': STATIC_URL
    }
    return HttpResponse(template.render(context, request))
