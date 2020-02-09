from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt="welcome to my repository, let'\s learn some python basics", ln=1,align="C")
pdf.cell(200,10,txt="This repo shows some of my beginer projects in python", ln=2,align="L")
pdf.cell(200,10,txt="This was created by MORYSO for learning tutorials", ln=2,align="L")
pdf.cell(200,10,txt="feel free to enjoy them", ln=2,align="L")
pdf.cell(200,10,txt="Thank you", ln=2,align="C")

pdf.output("pdf.pdf")
