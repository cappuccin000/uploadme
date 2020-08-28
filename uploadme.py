#!/usr/bin/python
print("<<==========UPLOAD ME==========>>")
print("            =========            ")
import subprocess
import sys, getopt
import os
import pyqrcode 
import png 
from pyqrcode import QRCode 
def main(argv):
   inputfile = ''
   outputfile = '1'
   try:
      opts, args = getopt.getopt(argv,"hf:e:",["file=","expiry="])
   except getopt.GetoptError:
      print("usage: python uploadme.py --f <inputfile> --e <expiry>")
      print(" --f(--file)\tfile to be uploaded")
      print(" --e(--expiry)\texpiry to be specified in weeks")
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
   cmd = "curl -F " + '"' + "file="  + "@" + inputfile + '"' + "  https://file.io/?expires=" + outputfile + "w"
   num = len(sys.argv)
   if(num == 3 or num == 5):
    os = sys.platform
    if(os in "win32" or os in "win64"):
     import os
     myCmd = os.popen(cmd).read()
     cmd=myCmd[45:73]
     print(cmd);
     url = pyqrcode.create(cmd)
     url.png('my.png', scale = 6)
     os.system('.\my.png')
    else:
     import os
     myCmd = os.popen(cmd).read()
     cmd=myCmd[45:73]
     url = pyqrcode.create(cmd)
     url.png('my.png', scale = 6)
     os.system('eog my.png')
   else:
    print("usage: python uploadme.py --f <inputfile> --e <expiry>")
    print(" --f(--file)\tfile to be uploaded")
    print(" --e(--expiry)\texpiry to be specified in weeks Default(1 week)")

if __name__ == "__main__":
   main(sys.argv[1:])

