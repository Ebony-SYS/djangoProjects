from django.shortcuts import render


def home(request):
    return render(request, 'mooc/home.html')


def contact(request):
    return render(request, 'mooc/contact.html')


def courses(request):
    return render(request, 'mooc/courses.html')
