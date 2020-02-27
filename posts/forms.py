from django import forms 
from .models import posts

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fiels = ('title', 'content', 'image', 'tag', 'published_date')