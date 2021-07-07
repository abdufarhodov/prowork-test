from django.shortcuts import render
from .models import Category, Photo

###########################################################

def index(request):
    objects = Photo.objects.all().order_by('-id')
    categories = Category.objects.all()
    context = {
        'objects': objects,
        'categories': categories
    }
    return render(request, 'index.html', context)

###############################################################

def detail(request, pk):
    categories = Category.objects.all()
    objects = Photo.objects.get(id=pk)
    context = {
        'el': objects,
        'categories':categories,
    }
    return render(request, 'detail.html', context)

###############################################################

def category(request, name):
    obj = Category.objects.get(name=name)

    objects = obj.photo_set.order_by("id")

    categories = Category.objects.all()

    context = {
        'objects': objects,
        'categories': categories,
    }

    return render(request, 'index.html', context)

############################################################

def search(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('search')
        objects = Photo.objects.filter(title__contains=name)
        context = {
            'objects':objects,
            'categories':categories,
        }
    else:
        context = None

    return render(request,'index.html',context)

#############################################################

def searchCat(request):
    if request.method == 'POST':
        name = request.POST.get('search')
        objects = Category.objects.filter(name__contains=name)
        context = {
            'objects':objects,
        }
    else:
        context = None

    return render(request,'index.html',context)