from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import Article, Comment
from django.http import JsonResponse
# from django.http import HttpResponse
# import json
# from django.utils.html import mark_safe
from django.core import serializers


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


# API
def all(request):
    article_list = Article.objects.all().order_by('-pub_date')[0]
    data = serializers.serialize("json", article_list)
    return JsonResponse({'article_list': data})

    # json_posts = mark_safe(json.dumps(list(article_list), ensure_ascii=False))

    # return HttpResponse(
    #     json_posts,
    #     content_type="application/json"
    # )
