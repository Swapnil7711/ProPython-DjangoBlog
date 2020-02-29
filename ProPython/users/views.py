from django.shortcuts import render, redirect
from .forms import UserRgisteForm, u_form, p_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.


def register(request):

    if request.method == "POST":
        form = UserRgisteForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, " Your account has been created successfully")
            return redirect("login")
    else:
        form = UserRgisteForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):

    if (request.method == "POST"):
        userform = u_form(request.POST, instance = request.user)
        profileform = p_form(request.POST, request.FILES , instance = request.user.profile)

        if (userform.is_valid() and profileform.is_valid()):
            
            userform.save()
            profileform.save()
            print(profileform["image"])
            
            messages.success(request, "successfully updated")
            return redirect("profile")

    else:
        userform = u_form(instance = request.user)
        profileform = p_form(instance = request.user.profile)   

    context = {
        "u_form" : userform,
        "p_form" : profileform,
    }
    
    

    return render(request, "users/profile.html", context)
