#This program will check for profanity of text in a file
import urllib

#open a file and read it
#@param the name of the file (with location relative from this program)
def read_text(file_name):
    f=open(file_name,"r")
    text=f.read()
    return text

#check if the file contains any profane word
#@param file to be checked(with location relative from this program)
def check_profanity(file_name):
    words=read_text(file_name)
    conn=urllib.urlopen("http://www.wdylike.appspot.com/?q="+words)
    output=conn.read()
    if "true" in output:
        print("Profanity alert!!!")
    elif "false" in output:
        print("Everything is fine..")
    else:
        print("something wrong")

check_profanity("movie_quotes.txt")




