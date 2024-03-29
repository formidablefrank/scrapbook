from datetime import date
from django.db import models
from django.utils import timezone
from django import forms
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader


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

    # Archive a scrapbook: just set its 'active' flag to 0.
    def archive(self):
        self.active = 0
        self.save()

    # Activate a scrapbook: just set its 'active' flag to 1.
    # Deactivate the activate scrapbook first before activating the current scrapbook.
    def activate(self):
        try:
            Scrapbook.objects.get(active = 1).archive()
        except Exception:
            pass
        self.active = 1
        self.save()

    # Generating pdf. Made possible by ReportLab library.
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

        photos = self.picture_set.all()
        lwidth, height = letter

        # Dedicate a photo and its information for a page.
        for photo in photos:
            p.translate(inch, inch)

            #Get the binary format of the image using its url
            image = ImageReader(photo.pic.url)
            p.drawImage(image, 0, -300, width=lwidth/4*3, preserveAspectRatio=True)

            p.drawString(0, 150, photo.name)
            p.drawString(0, 135, str(photo.date))
            p.drawString(0, 120, photo.caption)
            p.setFont("Helvetica-Bold", 30)
            p.drawString(0, 50, self.name)
            p.setFont("Helvetica", 12)
            p.drawString(0, 20, "A Life's Journey")
            p.drawString(0, 0, "Keeping memories that's better than ever.")
            p.showPage()

        #Close the PDF object cleanly.
        p.save()

        #Get the value of BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        # The response object that contains the pdf
        # is passed to the controller and passed immediately to the client for downloading
        return response


    # Get the active method. Returns that scrapbook or null.
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
    date = models.DateTimeField(auto_now_add = True, blank = True)
    pic = models.ImageField(upload_to = 'assets/scrapbooks/', default = 'assets/no-img.jpg')
