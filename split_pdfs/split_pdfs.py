import PyPDF2
import json

def get_start_end(s):
    if '-' in s:
        start, end = s.split('-')
        return int(start)-1, int(end)

    else:
        return int(s)-1, int(s)

def extract_pages(source_file, start, end, extract_name):
    # Initialize pdf reader and writer

    pdfWriter = PyPDF2.PdfFileWriter()

    
    pdfFile = open(source_file.strip(), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    

    for pageNum in range(start, end):
        pageObj = pdfReader.getPage(pageNum) # Extract Page
        pdfWriter.addPage(pageObj) # Write extracted page into new pdf file

    outputname = extract_name

    pdfOutputFile = open(outputname, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdfFile.close()

config = json.load(open('to_split.json', 'r'))


for source_file in config:
    for extract_name in config[source_file]:

        start, end = get_start_end(config[source_file][extract_name])
        extract_pages(source_file, start, end, extract_name)
