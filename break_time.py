#This program will remind you to take a break every interval (e.g. 1 hour) by opening youtube video for you
import webbrowser
import time

print("This program starts at "+time.ctime())
total_breaks=3
for i in range(total_breaks):
    time.sleep(1*3600) #sleep for 1 hour
    webbrowser.open("https://www.youtube.com/watch?v=BwK23wVt4KM")

