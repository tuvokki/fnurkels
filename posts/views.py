from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import Article, Comment


# Create your views here.
def index(request):
    article_list = get_list_or_404(Article.objects.order_by('-pub_date')[:5])
    context = {'article_list': article_list}
    return render(request, 'posts/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    context = {'article': article, 'comments': comments}
    return render(request, 'posts/detail.html', context)


def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    Comment.objects.create(
      article=article, text=request.POST['comment_text']
    )
    return redirect('posts:detail', article_id=article_id)
