from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')
    #path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
]