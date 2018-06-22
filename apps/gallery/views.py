from django.shortcuts import render_to_response
from gallery.models import Image, ImageType


# Create your views here.
def images_list(request):
    content = {}
    images_list = Image.objects.all()
    image_types = ImageType.objects.all()
    content['image_types'] = image_types
    content['images_list'] = images_list
    return render_to_response('gallery/index.html', content)


def image_type_list(request, image_type_pk):
    content = {}
    images_list = Image.objects.filter(img_type_id=image_type_pk)
    image_types = ImageType.objects.all()
    content['image_types'] = image_types
    content['images_list'] = images_list
    return render_to_response('gallery/index.html', content)


def about(request):
    content = {}
    image_types = ImageType.objects.all()
    content['image_types'] = image_types
    return render_to_response('gallery/about.html', content)


def contact(request):
    content = {}
    image_types = ImageType.objects.all()
    content['image_types'] = image_types
    return render_to_response('gallery/contact.html', content)
