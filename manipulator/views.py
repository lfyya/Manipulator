from django.shortcuts import render

def Main(request):
    return render(request, 'main.html')  # or 'myapp/home.html' if in app folder


def manipulator(request):
    return render(request, 'manipulator.html')
