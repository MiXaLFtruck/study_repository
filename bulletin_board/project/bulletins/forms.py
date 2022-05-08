from django import forms
from .models import Bulletin, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Bulletin
        fields = ['author', 'category', 'title', 'content', 'slug']
        widgets = {
            'slug': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
