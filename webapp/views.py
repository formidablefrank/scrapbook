from django.shortcuts import render, redirect
from .models import Scrapbook, Picture, ImageUploadForm
from datetime import date

# Create your views here.
def index(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'home/home.html', context)


def login(request):
    context = {'pagename': 'Login'}
    return render(request, 'home/login.html', context)


def dashboard(request):
    scrapbooks = Scrapbook.objects.filter(active = 0)
    activebook = Scrapbook.getActive()
    context = {'pagename': 'Home', 'books': scrapbooks, 'activebook': activebook}
    return render(request, 'dashboard/home.html', context)


def create(request):
    scrapbooks = Scrapbook.objects.filter(active = 0)
    activebook = Scrapbook.getActive()
    if request.POST:
        if activebook != 0:
            activebook.archive()

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
        new_scrap.active = 1
        new_scrap.save()
        return redirect('/webapp/view/' + str(new_scrap.id))

    context = {'pagename': 'Create Scrapbook', 'create': True, 'books': scrapbooks, 'activebook': activebook}
    return render(request, 'dashboard/create.html', context)


def view(request, book_id):
    scrapbooks = Scrapbook.objects.filter(active = 0)
    activebook = Scrapbook.getActive()
    book = Scrapbook.objects.get(id = book_id)
    current = False
    view = False
    if activebook == book:
        current = True
    else:
        view = True
    context = {'pagename': 'Create Scrapbook', 'current': current, 'view': view, 'book': book, 'books': scrapbooks, 'activebook': activebook}
    return render(request, 'dashboard/viewscrapbook.html', context)


def upload(request, book_id):
    if request.POST:
        book = Scrapbook.objects.get(id = book_id)
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_pic = Picture()
            new_pic.name = request.POST['name']
            new_pic.caption = request.POST['caption']
            new_pic.date = date.today().strftime('%Y-%m-%d')
            new_pic.pic = form.cleaned_data['image']
            book.picture_set.add(new_pic)
            book.save()
    return redirect('/webapp/view/' + book_id)


def archive(request, book_id):
    book = Scrapbook.objects.get(id = book_id)
    book.archive()
    return view(request, book_id)


def activate(request, book_id):
    book = Scrapbook.objects.get(id = book_id)
    book.activate()
    return view(request, book_id)


def publish(request, book_id):
    book = Scrapbook.objects.get(id = book_id)
    return book.generate_pdf()


def deleteBook(request, book_id):
    book = Scrapbook.objects.get(id = book_id)
    book.delete()
    return redirect('dashboard')


def deletePhoto(request, book_id, photo_id):
    picture = Scrapbook.objects.get(id = book_id).picture_set.get(id = photo_id)
    picture.delete()
    return view(request, book_id)
