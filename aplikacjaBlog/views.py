from django.shortcuts import render

from aplikacjaBlog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return "test 123"
