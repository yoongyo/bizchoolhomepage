from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')

def introduction(request):
    return render(request, 'homepage/introduction.html')


def subject(request):
    return render(request, 'homepage/subject.html')


def news(request):
    return render(request, 'homepage/news.html')


def entrance(request):
    return render(request, 'homepage/entrance.html')