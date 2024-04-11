from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from aplikacjaBlog.forms import CommentForm
from aplikacjaBlog.models import Post

#def post_list(request):
    #posts = Post.objects.all().filter(status='published')
    #return render(request, 'Blog/post/list.html', {"posts": posts})

class PostListView(ListView):
    queryset = Post.objects.all().filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'Blog/post/list.html'

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    comment_form = CommentForm()

    return render(request, 'Blog/post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

