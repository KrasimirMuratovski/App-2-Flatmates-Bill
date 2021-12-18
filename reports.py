import webbrowser
import os
from fpdf import FPDF
from filestack import Client

class PdfReport:
    """
    Creates a pdf file
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay=str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        flatmate2_pay=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image("files/house.png", w=30, h=30)

        #Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        #Insert period and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        #Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        os.chdir("files")
        pdf.output(self.filename)

        webbrowser.open(self.filename)

class FileSharer:
    #https://dev.filestack.com/apps/A1cnZbkRtQmuUUxWUeSPmz/dashboard/#
    def __init__(self, filepath, api_key='A1cnZbkRtQmuUUxWUeSPmz'):
        self.api_key = api_key
        self.filepath=filepath
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
