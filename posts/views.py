from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    return redirect("post-list")


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    curr_page_num = request.GET.get("page")
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    return render(request, "posts/post_list.html", {"page": page})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect("post-detail", post_id=new_post.id)
    else:
        post_form = PostForm()
    return render(request, "posts/post_form.html", {"form": post_form})


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("post-detail", post_id=post.id)
    else:
        post_form = PostForm(instance=post)
    return render(request, "posts/post_form.html", {"form": post_form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("post-list")
    else:
        return render(request, "posts/post_confirm_delete.html", {"post": post})
