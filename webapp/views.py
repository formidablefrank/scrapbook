from django.shortcuts import render
from .models import Scrapbook


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
    success = False
    if request.POST:
        new_scrap = Scrapbook(request.POST['name'], request.POST['description'], request.POST['start_date'], int(request.POST['frequency']), int(request.POST['every']), int(request.POST['mode']), request.POST['email'])
        new_scrap.save()
        success = True

    context = {'pagename': 'Create Scrapbook', 'create': True, 'success': success}
    return render(request, 'dashboard/create.html', context)
