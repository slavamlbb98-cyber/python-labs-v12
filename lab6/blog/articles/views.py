from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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

def register(request):
    form = {}

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        form = {"username": username, "email": email}

        if not username or not email or not password:
            form["errors"] = "Заполните логин, электронную почту и пароль."
        else:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                return redirect("archive")

            form["errors"] = "Пользователь с таким логином уже существует."

    return render(request, "register.html", {"form": form})

def login_view(request):
    form = {}

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        form["username"] = username

        if not username or not password:
            form["errors"] = "Введите логин и пароль."
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("archive")

            form["errors"] = "Неверный логин или пароль."

    return render(request, "login.html", {"form": form})