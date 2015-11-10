from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'webapp/home.html', context)


def create(request):
    context = {'pagename': 'Create Scrapbook'}
    return render(request, 'webapp/create.html', context)