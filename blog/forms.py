from django import forms
from django.forms import fields
from .models import Post, Document


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
