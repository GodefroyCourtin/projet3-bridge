
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import Signin, Signup
from .models import My_user
from django.contrib.auth.decorators import login_required


def inscription(request):
    """Display the sign up form."""
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = My_user.objects.create_user(username, email, password)
            user.last_name = form.cleaned_data["last_name"]
            user.first_name = form.cleaned_data["first_name"]
            user.save()
            return redirect("account:connexion")
    else:
        return render(
            request, "account/inscription.html", {"form": Signup()}
        )


def connexion(request):
    """Display the sign in form."""
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "account/connexion.html", {"form": Signin()})
    else:
        return render(request, "account/connexion.html", {"form": Signin()})

@login_required
def my_account(request):
    return render(request, "account/my_account.html")

    

@login_required
def deconnexion(request):
    """Allow the user to disconnect."""
    logout(request)
    return redirect('/')