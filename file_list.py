# Author: Brian Mukeswe
# Date: July 23, 2018
# Contact: b.mukeswe@sms.ed.ac.uk
# This script generates a text file containing a list of all files in a root directory and files in all subdirectories.
#     The output list includes the date and time at which each file was last modified
import os, sys
from time import gmtime, strftime
wd = os.getcwd()
     
fileobjct = open('file_list.txt','w')

for root, dirs, files in os.walk(wd):
    for filename in files:
        if len(os.path.join(root,filename)) < 256:
            file_m_time = os.path.getmtime(os.path.join(root,filename))
            file_m_time_fmt = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(file_m_time))
            fileobjct.write(str(file_m_time_fmt) + ' ' +filename + '\n')
        
fileobjct.close()
print("done")
