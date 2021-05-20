from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('file_upload/', views.upload, name='upload'),
    #path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
]