from django.shortcuts import render
from blog.models import Category


def stack(request):

    category = Category.objects.all()

    return render(
           request,
           "menu/stack.html",
           {"category": category,},
           )
