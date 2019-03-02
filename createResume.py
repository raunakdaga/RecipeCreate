from fpdf import FPDF

name = input("Name? ") # change to html
phone = input("Phone Number? ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.cell(50, 10, txt=name, ln=1, align="L")
pdf.cell(50, 10, txt=phone, ln=1, align="C")
pdf.output("simple_demo.pdf")
