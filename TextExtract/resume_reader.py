import PyPDF2
import textract
import re
from collections import defaultdict

def read_pdf(filename, output_filename = 'output.txt'):
    '''
    read pdf file and return text as string
    :param filename: pdf file path
    :return: text string
    '''

    # Open allows you to read the file
    pdfFileObj = open(filename, 'rb')

    # The pdfReader variable is a readable object that will be parsed
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Discerning the number of pages will allow us to parse through all #the pages
    num_pages = pdfReader.numPages
    count = 0
    text = ""

    # The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    # This if statement exists to check if the above library returned #words. It's done because
    # PyPDF2 cannot read scanned files.
    if text != "":
        text = text
    # If the above returns as False, we run the OCR library textract to #convert scanned/image
    # based PDF files into text
    else:
        text = textract.process(filename, method='tesseract', language='eng')

    text = text.decode('utf8')

    # Write to txt file
    # with open(output_filename, 'w') as f:
    #     f.write(text)

    return text
