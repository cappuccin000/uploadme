#!/usr/bin/python3
import sys
import os
operating = sys.platform
if(operating  in "win32" or operating in "win64"):
 os.system('pip3 install tkintertable')
 os.system('pip3 install pyqrcode')
 os.system('pip3 install pypng')
else:
 os.system('chmod +x uploadme.py')
 import os
 myCmd = os.popen('pwd').read()
 inputfile = "/uploadme.py"
 cmd = myCmd.rstrip("\n")
 cmd = cmd + inputfile
 command = "sudo ln -s " + cmd + " /usr/bin/uploadme"
 os.system(command)
 myCmd = os.popen('sed -i -e "s/\r$//" uploadme.py').read()
 os.system('sudo apt-get install python3-tk')
 os.system('pip3 install pyqrcode')
 os.system('pip3 install pypng')
 os.system('sudo apt-get install eog')
