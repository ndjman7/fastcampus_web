from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects\
        .filter(
            Q(published_date__lte=timezone.now()) |
            Q(published_date=None)
        ).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'title': '타이틀 변수는 title키를 이용해서 접근'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponse("로그인 하세요!")
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
