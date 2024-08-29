from django.shortcuts import render, get_object_or_404
from index.models import Article
from index.forms import EmailForm
from django.core.paginator import Paginator


def home(request):
    form = EmailForm()
    articles = Article.objects.order_by('-id')[:4]
    big_flover_article = Article.objects.filter(category='big_flover')[:6]
    all_categories = list(set(Article.objects.values_list('category', flat=True)))
    sport_article = Article.objects.filter(category='Sport')[:3]
    game_article = Article.objects.filter(category='Game')[:3]
    context = {
        "articles": articles,
        "all_categories": all_categories,
        "big_flover_article": big_flover_article,
        "sport_article": sport_article,
        "game_article": game_article,
        "form": form,
    }

    return render(request, 'index.html', context=context)

def single(request, pk):
    article = get_object_or_404(Article, pk=pk)
    all_categories = list(set(Article.objects.values_list('category', flat=True)))
    context = {
        "article": article,
        "all_categories": all_categories
    }
    return render(request, "single.html", context=context)


def categories(request):
    cat = request.GET.get("cat")
    articles = Article.objects.filter(category=cat)
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    page = request.GET.get("page")
    paginator = Paginator(articles, 2)
    article_page = paginator.get_page(page)

    context = {
        "articles": articles,
        "cat": cat,
        "all_categories": all_categories,
        "article_page": article_page,
        "page": page
    }
    return render(request, "categories.html", context=context)

def search(request):
    search = request.GET.get("search")
    all_categories = list(set(Article.objects.values_list('category', flat=True)))

    if search:
        articles = Article.objects.filter(title__icontains=search)
    else:
        articles = Article.objects.all()
    context = {
        "articles": articles,
        "all_categories": all_categories
    }

    return render(request, "search.html", context=context)