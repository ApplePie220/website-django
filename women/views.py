from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["Об этом замечтально сайте", "Добавить замечательную статью", "Обратная связб", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html',
                  {'posts': posts, 'menu': menu, 'title': 'Главная страница замечательного сайта'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Об этом потрясающем сайте'})


def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
