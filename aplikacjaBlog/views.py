from django.http import HttpResponse
from django.shortcuts import render

from aplikacjaBlog.models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Blog/post/list.html')
