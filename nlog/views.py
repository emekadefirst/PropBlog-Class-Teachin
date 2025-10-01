from django.shortcuts import render, get_object_or_404
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'detail.html', {'blog': blog})