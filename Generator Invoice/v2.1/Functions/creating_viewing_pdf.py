#Code-base developed by:
#https://medium.com/@asttrodev/tutorial-gerando-pdf-simples-com-reportlab-e-python-6b67e3692bef

#Importing canvas from reportlab library 
from reportlab.pdfgen import canvas

#declaring function 
def GeneratePDF(list_Names):
    try:

#With canvas.Canvas(archive.pdf) 
#creating canvas object that will be generate pdf archive 
#with inserted name and place. 
#In example was stored the object on pdf variable;
        name_pdf = input('Please, insert PDF name: ')
        pdf = canvas.Canvas('{}.pdf'.format(name_pdf))

#The function drawString(y,x,text) 
#uses a Cartesian plane with X and Y axes in the pdf sheet
#(page on A4 is setted by width=595.27; height=841.89).
#So with setted positions y = 247 and x = 700 
#to center on screen, after each name,age in list_Names
#will write each starting on position 700 
#and reducing x every time 
#finish writing a line with the name and age;
        x = 720
        for name,age in list_Names.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(name,age))

#pdf.setTitle(title) will add title on pdf;
        pdf.setTitle(name_pdf)

#pdf.setFont(Font Name, size) will select font and size for items;
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Guests List')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Name and Age')

#pdf.Save() will save all modifications 
#on specified path of canvas.Canvas() object;
        pdf.save()
        print('{}.pdf successful created!'.format(name_pdf))
    except:
        print('Error on generate {}.pdf'.format(name_pdf))

#Creating called variable list_Names of dictionary type tipo inserting some values;
list_Names = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}

#Call function GeneratePDF(list_Names) passing variable list_Names as argument;
GeneratePDF(list_Names)

def pdf_viewer(archive.pdf):
     print("Opening PDF")
