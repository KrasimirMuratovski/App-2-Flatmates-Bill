from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

amount=float(input("Please state the amount: "))
period=input("Please state the period in format mm/YYY: ")

name1=input("Please state your name: ")
name1_days_in_house=int(input(f"{name1} - please state tha days in the house: "))

name2=input("Please state thr name of the flatmate: ")
name2_days_in_house=int(input(f"{name2} - please state tha days in the house: "))


the_bill= Bill(amount=amount, period=period)
flatmate1= Flatmate(name=name1, days_in_house=name1_days_in_house)
flatmate2= Flatmate(name=name2, days_in_house=name2_days_in_house)

print(f"{flatmate1.name} pays:", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report= PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2,bill=the_bill)

file_sharer=FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())