from PyPDF2 import PdfFileReader, PdfFileWriter

'''
This function slices pdf
* pdffile - path to pdf file to slice
* outfile - path to sliced file
* startpage - num of start page (first page=1)
* endpage - end page of slice
All credits to: https://stackoverflow.com/questions/45144206/pypdf2-split-pdf-by-pages
'''
def pdfslice(pdffile, outfile, startpage, endpage):
    with open(pdffile, 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        for i in range(startpage-1, endpage):
            writer.addPage(reader.getPage(i))

        with open(outfile, 'wb') as outfile:
            writer.write(outfile)
