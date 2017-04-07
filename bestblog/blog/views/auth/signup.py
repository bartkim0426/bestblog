from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup(request):

    if (request.method=="POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        User.objects.create_user(
               username=username,
               password=password,
               email=email,
                )
        return redirect(
                "auth:login",
                )

    return render(
            request,
            "auth/signup.html",
            {},
            )
