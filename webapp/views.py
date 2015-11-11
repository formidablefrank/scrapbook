from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'home/home.html', context)


def login(request):
    context = {'pagename': 'Login'}
    return render(request, 'home/login.html', context)


def dashboard(request):
    context = {'pagename': 'Home'}
    return render(request, 'dashboard/home.html', context)


def create(request):
    context = {'pagename': 'Create Scrapbook', 'create': True}
    return render(request, 'dashboard/create.html', context)
