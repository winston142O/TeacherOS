#libraries used

import shutil #for copy/pasting
import os #many things


#set paths

target_path = r"C:\WebDriver\bin"

ver = input('Type "quit" to quit.\n\nChoose Chrome version (93, 94, 95)\n')

#Make target directory
try:
    os.makedirs(target_path)
except:
    ()

#Copy file to new path
while True:
    try:
        shutil.copyfile(fr"D:\profesoresiberia2\Prerequisites\Chrome\{ver}\chromedriver.exe", fr"{target_path}\chromedriver.exe")    #PROGRAM ONLY WORKS IF RELATIVE PATH CONTAINS NECESSARY FILES
        break
    except:
        if str.lower(ver) == "quit":
            break
        else:
            print("Invalid\n\n")
            ver = input('Type "quit" to quit.\n\nChoose Chrome version (93, 94, 95)\n')
