import os
import string

def rename_files():
    ##save the current working directory
    save_dir = os.getcwd()
    ##save the folder where are the photos
    photos_dir = r"C:\Users\Fernando\Documents\fernando\udacity\FSWD\clase 5\photos" 
    ##get the names of files of directory
    file_list = os.listdir(photos_dir)
    ##changue to the folder where are the photos
    os.chdir(photos_dir)
    ##loop throug the array of name files
    for file_name in file_list:
        ##remove the numbers in the string and rename the file with the new ones
        os.rename(file_name,string.translate(file_name,None,"0123456789"))
    ##back to the directory saved
    os.chdir(save_dir)

rename_files()