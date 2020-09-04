#!/usr/bin/python
print("<<==========UPLOAD ME==========>>")
print("            =========            ")
import subprocess
from tkinter import filedialog
from tkinter import *
import sys, getopt
import os
import pyqrcode 
import png 
from pyqrcode import QRCode 
def main(argv):
   inputfile = ''
   outputfile = '0'
   try:
      opts, args = getopt.getopt(argv,"hf:e:",["file=","expiry="])
   except getopt.GetoptError:
      print("usage: python uploadme.py --f <inputfile> --e <expiry>")
      print("OR")
      print("python uploadme.py (To launch GUI mode)")
      print(" --f(--file)\tfile to be uploaded")
      print(" --e(--expiry)\texpiry to be specified in days")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print("usage: python uploadme.py --f <inputfile> --e <expiry>")
         print(" --f(--file)\tfile to be uploaded")
         print(" --e(--expiry)\texpiry to be specified in weeks")
         sys.exit()
      elif opt in ("-f", "--file"):
         inputfile = arg
      elif opt in ("-e", "--expiry"):
         outputfile = arg
   no = len(sys.argv)
   if(no == 3 or no == 5):
    print("server's to upload the file *use other servers if the selected one did not work* ")   
    print("1)transfer.sh  limit 10GB and expiry also available")
    print("2)0x0.st     limit 512MB and expires in 30 day")
    print("3)file.io   limit 200MB - only one download")
    opt=input("enter the option number")
    if(opt == '1'):
     if(outputfile == '0'):
      outputfile=input("enter the expiry");
      cmd = "curl  -H" + ' "' + "Max-Days:"+ outputfile +'"' + " --upload-file ./" + inputfile + " https://transfer.sh/" + inputfile
    if(opt == '2'):
     cmd = "curl -F " + '"' + "file="  + "@" + inputfile + '"' + " https://0x0.st"
    if(opt == '3'):
     outputfile = '1'
     cmd = "curl -F " + '"' + "file="  + "@" + inputfile + '"' + " https://file.io/?expires=" + outputfile + "w"
   num = len(sys.argv)
   if(num == 3 or num == 5):
    print("Note:Using Command line mode you can launch GUI by simply typing python uploadme.py") 
    os = sys.platform
    if(os in "win32" or os in "win64"):
     import os
     print(cmd)
     myCmd = os.popen(cmd).read()
     if(len(myCmd) < 30):
      myCmd = myCmd[45:73] 
     if ('file' in myCmd or 'transfer' in myCmd or '0x0' in myCmd):
      print("creating QR code")
     else:
      print("****Please enter a valid file****")
      exit()     
     url = pyqrcode.create(myCmd)
     url.png('my.png', scale = 6)
     os.system('.\my.png')
    else:
     import os
     myCmd = os.popen(cmd).read()
     url = pyqrcode.create(myCmd)
     url.png('my.png', scale = 6)
     os.system('eog my.png')
   else:
    print("LAUNCHING GUI MODE ......")
    root = Tk()
    root.withdraw()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    win = root.filename
    command = "curl -F " + '"' + "file="  + "@" + win + '"' + "  https://file.io/?expires=" + outputfile + "w"
    import os
    res = os.popen(command).read()
    if('file.io' in res):
      print("creating QR code")
    else:
      print("****Please enter a valid file****")
      exit()     
    print(res[45:73])
    url = pyqrcode.create(res[45:73])
    url.png('my.png', scale = 6)
    import os
    om = sys.platform
    if(om in "win32" or om in "win64"):
     os.system('.\my.png')
    else:
     os.system('eog my.png')

if __name__ == "__main__":
   main(sys.argv[1:])

