from django.shortcuts import render


def auth_menu(request):
    return render(
            request,
            "menu/auth.html",
            {},
            )
