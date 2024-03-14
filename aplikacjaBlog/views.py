from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from aplikacjaBlog.models import Post

def post_list(request):
    posts = Post.objects.all().filter(status='published')
    return render(request, 'Blog/post/list.html', {"posts": posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return  render(request, 'blog/post/detail.html', {"post": post })