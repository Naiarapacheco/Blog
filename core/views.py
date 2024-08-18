from django.db.models import Q

from django.shortcuts import render

from content.models import Post

def home(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/home.html', {'posts': posts})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'core/search.html', {'posts': posts, 'query':query})
