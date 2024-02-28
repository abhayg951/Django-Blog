from django import forms
from .models import BlogPost, Category

cats_choices = list()
choices = Category.objects.all().values_list('name', 'name')

for i in choices:
    cats_choices.append(i)

print(cats_choices)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'title_tag', 'header_img' ,'author', 'category', 'body', 'snippets')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author_id', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(choices=cats_choices, attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippets': forms.TextInput(attrs={'class': 'form-control'})
        } 

class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'title_tag', 'body', 'snippets')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippets': forms.TextInput(attrs={'class': 'form-control'})
        } 