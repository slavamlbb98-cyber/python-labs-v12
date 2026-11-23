from django.shortcuts import render

from .models import Article


def archive(request):
    posts = Article.objects.order_by("-created_date", "-id")
    return render(request, "archive.html", {"posts": posts})
