from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from accounts.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')

    return render(request, 'articles/index.html', {"articles": articles})

def write(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.writer_id = request.user.id
            f.save()

            return redirect('articles:index')

    else:
        form = ArticleForm()

    return render(request, 'articles/write.html', {'form': form})

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article
    }

    return render(request, "articles/detail.html", context)

# def update(request, pk):
#     article = Article.objects.get(pk=pk)

#     if request.method == "POST":
#         form = ArticleForm(request.POST, instance=article)

#         if form.is_valid():
#             form.save()

#             return redirect("articles:detail", pk)
    
#     else:
#         form = ArticleForm(instance=article)

#     context = {
#         "form": form
#     }

#     return render(request, "articles/write.html", context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user != article.writer:
        return redirect("articles:index")

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article.title = form.data.get("title")
            article.content = form.data.get("content")
            article.save()
            return redirect("articles:detail", pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form
    }
    return render(request, "articles/write.html", context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user != article.writer:
        return redirect("articles:index")

    if request.method == "POST":
        if request.user == article.writer:
            article.delete()
            return redirect("articles:index")
    else:
        return redirect("articles:detail", pk)