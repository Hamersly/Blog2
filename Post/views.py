from django.shortcuts import render, get_object_or_404
from .models import Views


def news_list(request):
    news = Views.objects.all()
    return render(request, 'Post/news_list.html', {'news': news})


def new_single(request, pk):
    new = get_object_or_404(Views, id=pk)
    return render(request, 'Post/new_single.html', {'new': new})
