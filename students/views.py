from django.shortcuts import render


# Create your views here.

# Login view
def login(request):
    return render(request, 'students/login.html')


def home(request):
    return render(request, 'home.html')
