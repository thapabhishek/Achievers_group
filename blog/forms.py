from django import forms
from django.forms import fields
from .models import Post, Document, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')


class Subscribe(forms.Form):
    Email = forms.EmailField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')