from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User



def login(request):
    
    if (request.method=="POST"):
        next_page = request.POST.get("next_page") or "menu/auth.html"
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        
        if user:
            auth_login(request, user)
            return redirect(
                    next_page,
                    )
        else:
            return render(
                request,
                "auth/login.html",
                {},
                )
    
    return render(
        request,
        "auth/login.html",
        {},
        )
