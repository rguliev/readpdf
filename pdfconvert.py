import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

'''
This function converts pdf to one of formats: xml, html, txt (default)
* pdffile - path to pdf file to convert
* outfile - path to converted file
* outfmt  - format for converting: xml, html, txt
* pages   - list or tuple of pages to convert
All credits to https://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text
NOTE: For Python3 use pdfminer.six
'''
def pdfconvert(pdffile, outfile, outfmt = 'txt', pages = False):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()
    fmt_func_mapping = {'txt':TextConverter, 'htmp':HTMLConverter, 'xml':XMLConverter}
    with open(outfile, 'wb') as retstr:
        device = fmt_func[outfmt.lower()](rsrcmgr, retstr, codec=codec, laparams=laparams)
        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        with open(pdffile, 'rb') as fp:
            for page in PDFPage.get_pages(fp, pagenos=pages):
                interpreter.process_page(page)
