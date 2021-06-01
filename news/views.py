from django.shortcuts import render, get_object_or_404
from .models import New


def news_list(request):
    news = New.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context=context)


def news_detail(request, new_id):
    news = get_object_or_404(New, id=new_id)
    return render(request, 'news/news.html', {'news': news})
