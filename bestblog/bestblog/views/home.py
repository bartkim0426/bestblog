from django.shortcuts import render


def home(request):
    return render(
           request,
           "home.html",
           {'blog_name':'best_blog'}
           )
