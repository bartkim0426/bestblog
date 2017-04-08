from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    
    return redirect(
            "menu:auth",
            )
