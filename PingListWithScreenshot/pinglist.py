from selenium import webdriver
from time import sleep
import socket

filer = open('list.txt','r')
lines = filer.readlines()

driver = webdriver.Firefox()

output = []

for line in lines:
    outputline = ''
    try:
        
        driver.get("http://"+line.strip())
        sleep(1)
        try:
            driver.get_screenshot_as_file("./sceenshots/"+line.strip()+".png") 
            outputline="{},{}".format(line.strip(),socket.gethostbyname(line.strip()))
        except Exception as e:
            outputline="{},{},{}".format(line.strip(),socket.gethostbyname(line.strip(),"AUTH ALERT")
    except socket.gaierror:
        outputline="{},{}".format(line.strip(),"dead")
    output.append(outputline.strip()+"\n")
    print(outputline)

driver.quit()
filew = open('result.txt','w')
filew.writelines(output)
filew.close()