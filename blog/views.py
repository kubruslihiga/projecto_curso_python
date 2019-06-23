from django.shortcuts import render, redirect
from django.db import transaction
from blog.models import Post, Category
from blog.forms import CommentForm, PostForm
from blog.models import Comment
from blog.services import BlogServices


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            services = BlogServices()
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            services.add_comment(comment)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)


def open_post_page(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            category_ids = form.cleaned_data["categories"]
            if category_ids:
                post = Post(
                    title = form.cleaned_data["title"],
                    body = form.cleaned_data["body"],
                )
                postServices = BlogServices()
                postServices.insert_post(post, category_ids)
            return redirect('blog_index')
    context = {
        "form" : form
    }
    return render(request, "post.html", context)


def search(request):
    if request.method == "GET":
        param = request.GET.get('find_your_blog')
        if param:
            postServices = BlogServices()
            posts = postServices.search(param)
            context = { "posts": posts }
            return render(request, "blog_index.html", context)
    return blog_index(request)