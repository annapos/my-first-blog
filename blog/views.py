from django.shortcuts import render, get_object_or_4004
from django.db.models import Q

from example.config import pagination

# Create your views here.
from .models import Post, Category

def post_list(request):
    template = 'blog/post_list.html'
    object_list = Post.objects.filter(status='Published')

    pages = pagination(request, object_list,1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
    }   
    return render(request, template, context)

def post_detail(request, slug):
    template = 'blog/post detail.html'



    context = {
        'post': post,
    }
    return render(request,template,context)

def category_detail(request, slug)
    template = 'blog/category_detail.html'

    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category, status='Published')

    context = {
        'category': category,
        'post': post,
    }
    return render(request, template, context)


def search(request):
    template = 'blog/post_list.html'
    
    query = request.GET.get('q')

    results = Post.objects.filter(Q(title__icontains=query) | Q(body__incontains=query))

    pages = pagination(request, results, num=1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)