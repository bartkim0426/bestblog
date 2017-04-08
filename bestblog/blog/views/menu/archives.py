from django.shortcuts import render


def archives(request):
    return render(
           request,
           "menu/archives.html",
           {},
           )
