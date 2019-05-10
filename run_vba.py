# Entry by Brian Mukeswe on July 23, 2018
# This script can be used to run a vba macro from python.
# Inputs: A Maro enabled spreadsheeet (.xlsm)

import os
import win32com.client as O_Sys

FileName = "Macro_file.xlsm"
FilePath = os.path.join(os.getcwd(),FileName)

if os.path.exists(FilePath):
    xl = O_Sys.Dispatch("Excel.Application")
    xl.Workbooks.Open(Filename = FilePath, ReadOnly = 1)
    xl.Application.Run("Macro2")
    xl.Application.Quit()
    del(xl)
    
    print("test successful")
