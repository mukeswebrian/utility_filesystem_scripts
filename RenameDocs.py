# Author: Brian Mukeswe
# Date: October 16, 2017
# Contact: b.mukeswe@sms.ed.ac.uk

''' This script can be used to rename multiple files in different directories
    within a given root directory

    Inputs: 1. A text file list of all the files to be renamed. The file names here are NOT to be specified with their full path name
    '''
import os, sys
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

namelist = txt_to_list('master_doc_names.txt') #specify the text file of all files to be renamed i.e <filename>.<file extension>

for root, dirs, files in os.walk(wd):
    for filename in files:
        for name in namelist:
            if filename == name:
                count = count + 1
                newname = os.path.join(root,filename[:6]+'FILE NAME INDEX'+filename[5:]) #specify the formatting to be applied to new file names. 
                filename = os.path.join(root,filename)
                os.rename(filename,newname)
                print('oldname: '+filename+'\n'+'newname: '+newname+'\n')
print(str(count)+' Files renamed')
        
