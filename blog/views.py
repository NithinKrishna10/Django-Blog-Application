from django.shortcuts import render,get_list_or_404,redirect

from .models import Post
from .forms import CommentForm

# Create your views here.


def details(request,slug):
    # post = get_list_or_404(Post,slug=slug)
    post = Post.objects.get(slug=slug)
    # comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            # form.save()
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/details.html',{'post':post, 'form':form})