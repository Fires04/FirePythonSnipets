import socket

filer = open('list.txt','r')
lines = filer.readlines()

output = []

for line in lines:
    outputline = ''
    try:
        outputline="{},{}".format(line.strip(),socket.gethostbyname(line.strip()))
    except socket.gaierror:
        outputline="{},{}".format(line.strip(),"dead")
    output.append(outputline.strip()+"\n")
    print(outputline)

filew = open('result.txt','w')
filew.writelines(output)
filew.close()