from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from accounts.models import User


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

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

            return redirect("articles:detail", pk)
    
    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form
    }

    return render(request, "articles/write.html", context)