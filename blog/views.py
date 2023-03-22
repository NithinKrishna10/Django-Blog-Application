from django.shortcuts import get_object_or_404, render,get_list_or_404,redirect

from django.db.models import Q
from .models import Post,Category
from .forms import CommentForm


# Create your views here.


def details(request, category_slug, slug):
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

            return redirect('post_detail',category_slug = category_slug, slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/details.html',{'post':post, 'form':form})

def category(request, slug):
    # category = get_object_or_404(Category, slug=slug)
    category = Category.objects.get(slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})




def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})