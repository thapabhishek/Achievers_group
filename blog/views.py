from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, PageNotAnInteger

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'post_list.html', {'page':page, 'posts':posts})
#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

    
def home(request):
    return HttpResponse('Hey')

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})