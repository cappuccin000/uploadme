import sys
import os
operating = sys.platform
if(operating  in "win32" or operating in "win64"):
 os.system('pip3 install pyqrcode')
 os.system('pip3 install pypng')
else:
 os.system('pip3 install pyqrcode')
 os.system('pip3 install pypng')
 os.system('sudo apt-get install eog')

