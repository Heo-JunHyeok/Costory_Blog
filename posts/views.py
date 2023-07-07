from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    RedirectView,
)
from django.urls import reverse
from .models import Post
from .forms import PostForm


class IndexRedirectView(RedirectView):
    pattern_name = "post-list"


class PostListView(ListView):
    model = Post
    ordering = ["-dt_created"]
    paginate_by = 6

    # 생략 가능
    # template_name = "posts/post_list.html"    # default: 앱/(model)_list.html
    # context_object_name = "posts"             # default: object_list, (model)_list
    # page_kwarg = "page"                       # defaut: page


class PostDetailView(DetailView):
    model = Post

    # 생략 가능
    # template_name = "posts/post_detail.html"
    # # urls.py에서 int형 파라미터를 'pk'로 할 경우, 관련 코드 모두 'pk'로 변환해야 한다.
    # pk_url_kwarg = "post_id"
    # context_object_name = "post"              # default: object, (model)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    # 생략 가능
    # template_name = "posts/post_form.html"

    # post_id -> pk
    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.objects.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    # 생략 가능
    # template_name = "posts/post_form.html"
    # # detail과 동일
    # pk_url_kwarg = "post_id"

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.id})


class PostDeleteView(DeleteView):
    model = Post

    # 생략 가능
    # template_name = "posts/post_confirm_delete.html"
    # # detail과 동일
    # pk_url_kwarg = "post_id"
    # context_object_name = "post"

    def get_success_url(self):
        return reverse("post-list")


# ---------------------------------------------------------------------------------------

# FBV(Funtion Based View)


# def index(request):
#     return redirect("post-list")


# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     curr_page_num = request.GET.get("page")
#     if curr_page_num is None:
#         curr_page_num = 1
#     page = paginator.page(curr_page_num)
#     return render(request, "posts/post_list.html", {"page": page})


# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, "posts/post_detail.html", {"post": post})


# def post_create(request):
#     if request.method == "POST":
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect("post-detail", post_id=new_post.id)
#     else:
#         post_form = PostForm()
#     return render(request, "posts/post_form.html", {"form": post_form})


# def post_update(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == "POST":
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect("post-detail", post_id=post.id)
#     else:
#         post_form = PostForm(instance=post)
#     return render(request, "posts/post_form.html", {"form": post_form})


# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == "POST":
#         post.delete()
#         return redirect("post-list")
#     else:
#         return render(request, "posts/post_confirm_delete.html", {"post": post})


# --------------------------------------------------------------------------------------

# CBV(import View)


# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, "posts/post_form.html", {"form": post_form})

#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect("post-detail", post_id=new_post.id)
#         return render(request, "posts/post_form.html", {"form": post_form})
