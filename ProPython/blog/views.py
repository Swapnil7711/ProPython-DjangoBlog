from django.shortcuts import render

# Create your views here.


posts = [
    {
        "author": "swapnil",
        "title": "First blog 1",
        "content": "first content",
        "date_posted": "Dec 19, 2019",
    },
    {
        "author": "swapnilH",
        "title": "First blog 2",
        "content": "second content",
        "date_posted": "Dec 20, 2019",
    },
]


def home(request):

    context = {
        "posts": posts,
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")

