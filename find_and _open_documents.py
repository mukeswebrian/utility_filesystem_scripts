# Author: Brian Mukeswe
# Date: October 16, 2017
# Contact: b.mukeswe@sms.ed.ac.uk

''' This script can be used to search for and open multiple files in different directories
    within a given root directory (usally the working directory)

    Inputs: 1. A text file list of all the files to be ropened. The file names here are NOT to be specified with their full path name
    '''
import os, sys, subprocess
wd = os.getcwd()
count = 0

def txt_to_list(txtfile=''):
    fileobjct = open(txtfile,'r')
    templist = fileobjct.readlines()
    outlist = []

    for name in templist:
        name = name.replace('\n','')
        outlist.append(name)

    return outlist

namelist = txt_to_list('files_of_interest.txt') #specify the text file of all files to be opened <filename>.<file extension>

for root, dirs, files in os.walk(wd):
    for filename in files:
        for name in namelist:
            if filename == name:
                count = count + 1 
                filename = os.path.join(root,filename)
                subprocess.Popen(['C:\Program Files (x86)\Microsoft Office\Office14\EXCEL.EXE',filename])
                print('File Opened: '+filename)
print(str(count)+' Files opened')
        
