from django.shortcuts import render_to_response
from gallery.models import ImageType
from blog.models import Article

# Create your views here.
def index(request):
    content = {}
    image_types = ImageType.objects.all()
    articles_list = Article.objects.all()[:3]
    content['image_types'] = image_types
    content['articles_list'] = articles_list

    return render_to_response('home.html', content)
