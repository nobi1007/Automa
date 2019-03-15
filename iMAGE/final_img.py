from PIL import Image, ImageDraw, ImageFont
import csv
image = Image.open('Edit Offer Letter Template.jpg')
draw =ImageDraw.Draw(image)
font = ImageFont.truetype('Calibri.ttf',size=48)
(x,y) = (405,770)
(x2,y2) = (427,603)
color = 'rgb(0,0,0)'
with open('Offer Letters Candidates.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        name = row[1]
        date = row[0]
        color2 = 'rgb(255,255,255)'
        draw.rectangle(((424,603),(700,650)),fill = color2)
        draw.rectangle(((402,760),(550,820)),fill = color2)
        draw.text((x,y),name,fill = color,font = font)
        draw.text((x2,y2),date,fill = color,font = font)
        image.save("Offer Letter "+name+".jpg")
csvFile.close()

