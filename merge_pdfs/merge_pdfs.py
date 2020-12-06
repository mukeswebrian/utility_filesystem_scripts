'''
Author: Brian  Mukeswe
Email: mukeswebrian@yahoo.com

This script can be used to merge PDFs
Inputs:
    1. a text file called 'files_to_merge.txt' listing the names of the pdfs
       to be merged in the order that they should appear in the output document.
    2. The pdf file to be merged must be in the same directory as this script

Outputs:
    1. a pdf file called 'merged.pdf'
'''


import PyPDF2

files = open('files_to_merge.txt', 'r').readlines()

# Initialize pdf reader and writer

pdfWriter = PyPDF2.PdfFileWriter()

for filename in files:
    pdfFile = open(filename.strip(), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    

    for pageNum in range(pdfReader.getNumPages()):
        pageObj = pdfReader.getPage(pageNum) # Extract Page
        pdfWriter.addPage(pageObj) # Write extracted page into new pdf file

outputname = 'merged.pdf'

pdfOutputFile = open(outputname, 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()
