from django.db import models
from django.utils import timezone
from django import forms
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


# Create your models here.
class Scrapbook(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    start_date = models.DateField(default = timezone.now)
    frequency = models.IntegerField(default = 0)
    every = models.IntegerField(default = 0)
    mode = models.IntegerField(default = 0)
    email = models.EmailField(max_length = 50, blank = True)
    active = models.IntegerField(default = 1)

    def archive(self):
        self.active = 0
        self.save()

    def activate(self):
        try:
            Scrapbook.objects.get(active = 1).archive()
        except Exception:
            pass
        self.active = 1
        self.save()

    def generate_pdf(self):
        #Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        tempname = 'attachment; filename="' + self.name + ' - A Life\'s Journey.pdf"'
        response['Content-Disposition'] = tempname

        buffer = BytesIO()
        #Create the PDF object, using the BytesIO object as its 'file'.
        p = canvas.Canvas(buffer)

        #Draw things on the PDF. Here's where the PDF generation happens.
        #See the ReportLab documentation for the full list of functionality.
        p.translate(inch, inch)
        p.drawString(0, 50, self.name)
        p.drawString(0, 25, "A Life's Journey")
        p.drawString(0, 0, "Keeping memories that's better than ever.")

        photos = self.picture_set.all()
        #for photo in photos:
            #p.drawImage(photo.pic, 100, 100)

        #Close the PDF object cleanly.
        p.showPage()
        p.save()

        #Get the value of BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    @staticmethod
    def getActive():
        try:
            return Scrapbook.objects.get(active = 1)
        except Exception:
            return 0


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class Picture(models.Model):
    scrapbook = models.ForeignKey(Scrapbook)
    name = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 20)
    date = models.DateTimeField()
    pic = models.ImageField(upload_to = 'assets/scrapbooks/', default = 'assets/no-img.jpg')
