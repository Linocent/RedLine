from django.shortcuts import render


def index(request):
    return render(request, "redline_car/index.html")
