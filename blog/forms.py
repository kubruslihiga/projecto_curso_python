from django import forms
from blog.models import Category

all_categories = []
for c in Category.objects.all():
    all_categories.append((c.pk, c.name))

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class PostForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Post title"
        })
    )
    body = forms.CharField(
        required=False,
        widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Write your post"
        })
    )
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=all_categories
    )
    