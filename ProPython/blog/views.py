from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Contact, Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


# posts = [
#     {
#         "author": "swapnil",
#         "title": "First blog 1",
#         "content": "first content",
#         "date_posted": "Dec 19, 2019",
#     },
#     {
#         "author": "swapnilH",
#         "title": "First blog 2",
#         "content": "second content",
#         "date_posted": "Dec 20, 2019",
#     },
# ]


def home(request):

    context = {
        "posts": Post.objects.all(),
    }

    return render(request, "blog/home.html", context)

class PostListView(ListView):
    model = Post

    paginate_by = 2

    template_name = "blog/home.html"

    context_object_name = "posts"

    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):

        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.id == post.author_id:
            return True
        else:
            return False          


class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post

    success_url = '/'

    def test_func(self):

        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False    



def about(request):
    return render(request, "blog/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        description = request.POST["description"]
        print(name, email)
        if len(name) < 2 or len(email) < 4 or len(description) < 10:
            messages.error(request, "Please enter valid information")
        else:
            contact = Contact(name=name, email=email, description=description)
            contact.save()
            messages.success(request, "Your information has successfully sent")

    return render(request, "blog/contact.html")


def search(request):
    param = request.GET["query"]

    if len(param) > 50:
        posts = Post.objects.none()
    else:
        postsTitle = Post.objects.filter(title__icontains=param)
        postsContent = Post.objects.filter(content__icontains=param)
        posts = postsTitle.union(postsContent)
    if posts.count() == 0:
        messages.warning(request, "No search results found, Please provide valid query")
    context = {"posts": posts, "query": param}
    return render(request, "blog/search.html", context)

