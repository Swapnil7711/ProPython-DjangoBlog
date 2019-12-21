from django.shortcuts import render
from .models import Contact, Post
from django.contrib import messages

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
    posts = Post.objects.filter(title__icontains=param)
    context = {"posts": posts}
    return render(request, "blog/search.html", context)

