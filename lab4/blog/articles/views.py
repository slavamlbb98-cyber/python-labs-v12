from django.shortcuts import get_object_or_404, render

from .models import Article


def archive(request):
    posts = Article.objects.order_by("-created_date", "-id")
    return render(request, "archive.html", {"posts": posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, "article.html", {"post": post})
