import PyPDF2

pdffileobj = open('file.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)

x = pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

f = open("/home/net/MORYSO/PYTHON/class tutorials/projects_1a/pdf to txt\\file2.txt","a")
f.writelines(str(line) for line in pdffileobj)
f.close()
