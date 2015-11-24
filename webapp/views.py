from django.shortcuts import render
from .models import Scrapbook
from datetime import date
import time

# Create your views here.
def index(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'home/home.html', context)


def login(request):
    context = {'pagename': 'Login'}
    return render(request, 'home/login.html', context)


def dashboard(request):
    scrapbooks = Scrapbook.objects.all()
    activebook = Scrapbook.objects.last()
    context = {'pagename': 'Home', 'books': scrapbooks, 'activebook': activebook}
    return render(request, 'dashboard/home.html', context)


def create(request):
    success = False
    activebook = Scrapbook.objects.last()
    scrapbooks = Scrapbook.objects.all()
    if request.POST:
        myDate = request.POST['start_date'].split('/')
        newDate = date(int(myDate[2]), int(myDate[0]), int(myDate[1]))
        new_scrap = Scrapbook()
        new_scrap.name = request.POST['name']
        new_scrap.description = request.POST['description']
        new_scrap.start_date = newDate.strftime('%Y-%m-%d')
        new_scrap.frequency = request.POST['frequency']
        new_scrap.every = request.POST['every']
        new_scrap.mode = request.POST['mode']
        new_scrap.email = request.POST['email']
        new_scrap.save()
        success = True

    context = {'pagename': 'Create Scrapbook', 'create': True, 'success': success, 'books': scrapbooks, 'activebook': activebook}
    return render(request, 'dashboard/create.html', context)


def view(request, book_id):
    scrapbooks = Scrapbook.objects.all()
    activebook = Scrapbook.objects.last()
    book = Scrapbook.objects.get(id = book_id)
    current = False
    view = False
    if activebook == book:
        current = True
    else:
        view = True
    context = {'pagename': 'Create Scrapbook', 'current': current, 'view': view, 'book': book, 'books': scrapbooks, 'activebook': activebook}
    return render(request, 'dashboard/view.html', context)
