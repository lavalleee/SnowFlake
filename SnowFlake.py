###############################
#          SnowFlake          #         
#                             #
#     Coded by lavalleee      #
###############################

#Importing Modules 
import os 
from tkinter import *
import time
import requests
import re
from bs4 import BeautifulSoup

# TKinter Setup
if __name__ == '__main__':    
    window = Tk()
    window.geometry("640x480")
    window.resizable(width=False, height=False)
    window.title("SnowFlake")
    bg = PhotoImage(file = "Fix")
    bgfill= Label(window, i=bg)
    bgfill.place(x=0, y=0)
# If/Else to Determine Greeting! 
    greet = ""
    result = time.localtime()
    hour = int(result.tm_hour)
    user= os.getlogin()
    if 4 <= hour <= 11:
        greet = ("Good Morning")
    elif 12 <= hour <= 17:
        greet = ("Good Afternoon")
    else:
        greet = ("Good Evening")

    greeting = Label(text=f"{greet}, {user}!",fg="white",)
    greeting.pack()

# Defines Zipcode Variable
    zipcode=StringVar()

# Function to handle zip code interpretation 
    def get_zip():
    # Gets the Zip
        zip = zipcode.get()
        link = f"https://weather.com/weather/today/l/{zip}"
        req = requests.get(link)
    # Scraping Link for Keyword that indicates Snow
        soup= BeautifulSoup(req.content, "html.parser")
        snow= str(soup.find('span', {'class':'BentoBox--value--1RWs5'})) 
    # Convert output to Readable Form
        twentyfourhr = str(re.sub('<[^>]+>','',snow))
        print (twentyfourhr)
    # If/Else to Output Whether There's Snow or Not  
        if twentyfourhr == "None" or twentyfourhr == "0 in":
            a = ("Inputted ZIP is either invalid, \nor no snow has fallen.")
        elif twentyfourhr != "None" or "0 in":
            a = (f"It has snowed {twentyfourhr} within the last 24 hours.")
        else:
            print(a)
            exit
    # Output Results to the Screen
        result = Label(window,width=35,fg= 'white',text=(f"{a}"), bg = '#79b6ec').place(x=180, y=245)

    Button1= Button(window, fg= 'white',text='Check', bg= '#79b6ec',command=get_zip).place(x=280, y=90)

    snowentry = Entry(window,fg='white', textvariable=zipcode, bg='#79b6ec',width=15).place(x=144, y=95)



window.mainloop()
