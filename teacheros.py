## Modules ##

import tkinter
from tkinter import *
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ctypes import *

## Notes ##


## Selenium setup ##

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.minimize_window()

## Global Variables ##

url = 'https://accounts.google.com/signin/v2/identifier?hl=es-419&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'


def signin(email):
    driver.maximize_window()
    driver.get(url)
    einput = driver.find_element_by_id("identifierId")
    einput.send_keys(email)
    einput.send_keys(Keys.RETURN)

## Functions ##

def winstonsignin():
    signin('')
 
def sandrasignin():
    signin('')

def leonelsignin():
    signin('')

def danilosignin():
    signin('')

def leisysignin():
    signin('')

def naydysignin():
    signin('')

def nicolesignin():
    signin('')

def henrysignin():
    signin('')

def alejandrosignin():
    signin('')
        
def gracesignin():
    signin('')

def aurorasignin():
    signin('')


## ALTERNATIVE WINDOWS ##

def englishsignin():
    window=Tk()
    window.title('Who are you?')
    englishframe = Frame(window)
    window.config(bg='dark blue')
    window.resizable(0, 0)
    englishframe.pack()
    window.geometry('90x25+360+200')
    bottomenglishframe = Frame(window)
    bottomenglishframe.pack( side = BOTTOM )
    danilobutton = Button(englishframe, text='Danilo', fg = 'white', bg='dark blue', command = danilosignin) 
    danilobutton.pack( side = LEFT )
    henrybutton = Button(englishframe, text='Henry', fg = 'white', bg='dark blue', command = henrysignin) 
    henrybutton.pack( side = LEFT )

def moreteachers():
    windowmore=Tk()
    windowmore.title('Más profesores')
    moreframe = Frame(windowmore)
    windowmore.config(bg='dark blue')
    windowmore.resizable(0, 0)
    moreframe.pack()
    windowmore.geometry('94x25+850+200')
    bottomenglishframe = Frame(windowmore)
    bottomenglishframe.pack( side = BOTTOM )
    nicolebutton = Button(moreframe, text='Nicole', fg = 'white', bg='dark blue', command = nicolesignin) 
    nicolebutton.pack( side = LEFT )
    winstonbutton = Button(moreframe, text= 'Winston', fg= 'white', bg='dark blue', command = winstonsignin)
    winstonbutton.pack()



## Window design ##

root = Tk()
root.title('TeacherOS')
frame = Frame(root)
root.config(bg='dark blue')
root.resizable(0, 0) # Removes maximize button #
frame.pack()
image1 = Image.open('iberialogo.png')
image1.resize((20,20))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=-2, y=25)
root.geometry('400x250+450+200')
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

## Buttons ##

englishbutton = Button(frame, text = 'English', fg ='white', bg='dark blue',command=englishsignin)
englishbutton.pack( side = LEFT )
aurorabutton = Button(frame, text = 'Aurora', fg ='white', bg='dark blue',command=aurorasignin)
aurorabutton.pack( side = LEFT)
gracebutton = Button(frame, text = 'Grace', fg ='white', bg='dark blue',command=gracesignin)
gracebutton.pack( side = LEFT )
leisybutton = Button(frame, text = 'Leisy', fg ='white', bg='dark blue',command=leisysignin)
leisybutton.pack( side = LEFT )
naydybutton = Button(frame, text = 'Naydy', fg ='white', bg='dark blue',command=naydysignin)
naydybutton.pack( side = LEFT )
leonelbutton = Button(frame, text = 'Leonel', fg ='white', bg='dark blue',command=leonelsignin)
leonelbutton.pack( side = LEFT )
sandrabutton = Button(frame, text = 'Sandra', fg ='white', bg='dark blue',command=sandrasignin)
sandrabutton.pack( side = LEFT )
alejandrobutton = Button(frame, text = 'Alejandro', fg ='white', bg='dark blue',command=alejandrosignin)
alejandrobutton.pack( side = LEFT )
plusbutton = Button(frame, text = 'MÁS', fg ='white', bg='dark blue',command=moreteachers)
plusbutton.pack(side=TOP)

## Run APP ##


root.mainloop()
