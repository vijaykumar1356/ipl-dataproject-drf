from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, 'app/home.html')


def problem1(request, *args, **kwargs):
    return render(request, "app/problem1.html")


def problem2(request, *args, **kwargs):
    return render(request, 'app/problem2.html')


def problem3(request, *args, **kwargs):
    return render(request, 'app/problem3.html')


def problem4(request, *args, **kwargs):
    return render(request, 'app/problem4.html')


def userstories(request, *args, **kwargs):
    return render(request, 'app/userstories.html')
