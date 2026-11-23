from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from .models import Article


def archive(request):
    posts = Article.objects.order_by("-created_date", "-id")
    return render(request, "archive.html", {"posts": posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, "article.html", {"post": post})

def create_post(request):
    if not request.user.is_authenticated:
        raise Http404

    form = {}

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()
        form = {"title": title, "text": text}

        if not title or not text:
            form["errors"] = "Введите название и описание работы."
        elif Article.objects.filter(title=title).exists():
            form["errors"] = "Работа с таким названием уже существует."
        else:
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user,
            )
            return redirect("get_article", article_id=article.id)

    return render(request, "create_post.html", {"form": form})