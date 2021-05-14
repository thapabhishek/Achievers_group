from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

    
def home(request):
    return HttpResponse('Hey')

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})