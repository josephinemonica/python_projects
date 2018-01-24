#This program will rename the files inside the folder prank/prank to reveal secret message
#Unzip the prank.zip folder to get the folder containing secret message
import os

def rename_files():
    #Get all of the file names in the dir
    file_list=os.listdir("prank/prank")
    print(file_list)
    #Rename them
    for file_name in file_list:
        os.rename("prank/prank/"+file_name,"prank/prank/"+file_name.translate(None,"0123456789"))

rename_files()
