from django import forms
from blog.models import Category

#all_categories = []
#for c in :
#    all_categories.append((c.pk, c.name))

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

    class CategoriesMultipleChoiceField(forms.ModelMultipleChoiceField):
        def label_from_instance(self, obj):
            return obj

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
    categories = CategoriesMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.all()
    )
    