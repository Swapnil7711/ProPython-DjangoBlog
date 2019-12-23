from django.shortcuts import render, redirect
from .forms import UserRgisteForm
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == "POST":
        form = UserRgisteForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, " Your account has been created successfully")
            return redirect("blog-home")
    else:
        form = UserRgisteForm()

    return render(request, "users/register.html", {"form": form})

