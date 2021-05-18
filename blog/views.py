from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

    
def home(request):
    return HttpResponse('Hey')

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})