'''
Author: Brian Mukeswe
Company: Midgard Consulting Inc.
Date: May 16, 2019
Contact: b.mukeswe@sms.ed.ac.uk


This script extracts comment pages and reference
information from a pdf file

'''
import tika
from tika import parser
import pandas as pd
import PyPDF2

def read_header_info(page_text):
    '''
    custom function to read header information given a block of text from a PDF page
    '''
    header = [] # store extracted items
    lines = page_text.split("\n") # split page text into lines
    count = 0 # count numbe rof extracted items
    
    key_words = ["Exhibit", "Tab", "Schedule", "Page"]
    
    # Extract header information
    for line in lines:
        for word in key_words:
            if word in line:
                header.append(line)
                count += 1
        if count >= 4:
            break
            
    # Format header information
    reference = ''
    for i in range(len(header)):
        reference = reference + "," +header[i]
    return reference[1:]    # skip comma at the begining of return string


def extract_pages(start, end, filename):
    '''
    Custom function to extracta specified range of pages from a pdf file
    '''
    pdfFile = open(filename, 'rb')
    
    # Initialize pdf reader and writer
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    
    for pageNum in range(start-1, end): # offset is required on start in order to get the correct page
        pageObj = pdfReader.getPage(pageNum) # Extract Page
        pdfWriter.addPage(pageObj) # Write extracted page into new pdf file
        
    outputname = "Page-" + str(pageNum+1) + "-extracted.pdf"
        
    # publish extracted pages
    pdfOutputFile = open(outputname, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdfFile.close()
        
    #print('Successfully extracted file: '+outputname)
    #print('Done extracting from: '+filename)
    
    return  outputname



if __name__ == "__main__":
    
    filename = "HOSSM_APPL_20180726 (CO IRs and Comments).pdf"
    comments = "comments.csv"
    headings = ["Type","Page","Author","Annotation","Date","Comment","Reference","Preamble", "Questions"]
    
    formatted_irs = pd.read_csv(comments, names=headings) 
    pages = formatted_irs["Page"]

    for i in range(len(formatted_irs)):
    
        to_extract = pages.iloc[i]
        
        # extract single page
        extract = extract_pages(to_extract, to_extract, filename)
    
        # read the text contents of the extracted pdf
        extract_info = parser.from_file(extract)["content"]
    
        # Store the reference information of the extracted pdf
        formatted_irs.Reference.iloc[i] = read_header_info(extract_info)
        
        # Include one page before and one page after
        extract_pages(to_extract-1, to_extract+1, filename) 
        
    formatted_irs.to_excel(comments.replace(".csv","-referenced.xlsx"))

