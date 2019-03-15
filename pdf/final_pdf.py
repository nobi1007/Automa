from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib import colors
pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
pdfmetrics.registerFont(TTFont('CALIBRIB', 'CALIBRIB.ttf'))

#------------------------------------------------

with open('Offer Letters Candidates.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        name = row[1]
        date = row[0]
#-------------------------------------------------
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFillColorRGB(1,1,1)
        can.rect(95,645,120,15, fill=1,stroke=0)
        can.rect(103,689,120,20, fill=1,stroke=0)
        can.setFillColorRGB(0,0,0)
        can.setFont('Calibri',12)   
        can.drawString(97, 649, name)
        can.setFont('Calibri',12)
        can.drawString(104, 689, date)
        can.save()
#--------------------------------------------------
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        existing_pdf = PdfFileReader(open("Offer Letter Template.pdf", "rb"))
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        outputStream = open("Offer Letter "+name+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
csvFile.close()


