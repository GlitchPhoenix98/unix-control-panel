import os
import time
import sys
sys.tracebacklimit = 0
os.system("clear")
os.system("figlet UCP")
print("1. Neofetch")
print("2. Htop")
print("3. Reboot")
print("4. Terminal")
opt = input ()
if opt == ('1'):
    os.system("clear")
    os.system("neofetch")
    time.sleep(3)
    os.system("clear")
    time.sleep(0.5)
    os.execv(sys.executable, ['python'] + sys.argv)
if opt == ('2'):
    os.system("htop")
    os.execv(sys.executable, ['python'] + sys.argv)
if opt == ('3'):
    os.system("reboot")
