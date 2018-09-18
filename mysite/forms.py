from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 100}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 100}))
    category = forms.ChoiceField
    image = forms.ImageField

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'category']
