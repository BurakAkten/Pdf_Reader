#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: aktenburakk
"""

import sys

#control of version(Python)
_2x_metni ="""
To run this code on your computer , the version of Python you are using must be 2 !!"""

try:
    if sys.version_info.major != 2:
        print(_2x_metni)
except AttributeError:#2.7 nın altındaki sürümlerde bu hata verilir.
    print(_2x_metni)

#usage control
args = sys.argv
if len(args) < 2:
    print ("Usage : <directory_path_for_pdf_files>!!")
    sys.exit()



#import locale 
#locale.setlocale(locale.LC_ALL, "tr_TR")

import PyPDF2 as pp2 # To read a pdf file
# to read dir and control every item is file
from os import listdir 
from os.path import isfile , join

#Read the directory that is in dir_path
#if the parameter which_file is given , then special files will be readed
#lastl returns file names in list
def read_dir(dir_path , which_file = ""):
    
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    
    if len(which_file) != 0:
        only_pdf_files = [pdf for pdf in onlyfiles if pdf[-4 :] == which_file]
        return only_pdf_files
    else:
        return onlyfiles

#the function read the pdf files and write the text from these pdf file into txt files
def read_pdf_write_to_text(in_dir,file_name , out_dir):
    

    pdf = open(in_dir+"/"+file_name ,"rb")
    

    output = open( out_dir+"/"+file_name[0:-4] , "w+")
    
    pdf_obj = pp2.PdfFileReader(pdf , False )

    
    num_of_pages = pdf_obj.numPages
    
    for i in range(num_of_pages):
        page = pdf_obj.getPage(i)
    
        page_text = page.extractText()
        
        output.write(page_text.encode("utf-8"))
        

if __name__ == '__main__':
    

    dir_path = sys.argv[1]
    files = read_dir(dir_path)
    result_path = "./results"
    for file in files:
        read_pdf_write_to_text(dir_path , file , result_path)




