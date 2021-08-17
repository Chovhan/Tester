import time
from pywinauto.application import Application


print("!!!! This is python file !!!!")
app = Application().start('notepad.exe', timeout=10)
time.sleep(5)