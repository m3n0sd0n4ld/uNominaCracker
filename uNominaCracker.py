#!/usr/bin/python
#####################################################
# uNominaCracker v.1.0
# Author: @David_Uton (M3n0sD0n4ld)
# Twitter: https://twitter.com/David_Uton
# Linkedin: https://www.linkedin.com/in/david-uton/
# Github: https://github.com/m3n0sd0n4ld
#####################################################
import sys, zipfile, signal
from pwn import *
from datetime import datetime

# Variables
letter = 'TRWAGMYFPDXBNJZSQVHLCKE'
showTime = datetime.now()

# Colors
blue = '\033[94m'
red = '\033[91m'
green = '\033[92m'
white = '\033[97m'
yellow = '\033[93m'
bold = '\033[1m'
end = '\033[0m'

# Functions
# Logotype
def logotype():
    print('''

█──█ ░█▄─░█ █▀▀█ █▀▄▀█ ─▀─ █▀▀▄ █▀▀█ ░█▀▀█ █▀▀█ █▀▀█ █▀▀ █─█ █▀▀ █▀▀█ 
█──█ ░█░█░█ █──█ █─▀─█ ▀█▀ █──█ █▄▄█ ░█─── █▄▄▀ █▄▄█ █── █▀▄ █▀▀ █▄▄▀ 
─▀▀▀ ░█──▀█ ▀▀▀▀ ▀───▀ ▀▀▀ ▀──▀ ▀──▀ ░█▄▄█ ▀─▀▀ ▀──▀ ▀▀▀ ▀─▀ ▀▀▀ ▀─▀▀
                                            by %s%sM3n0sD0n4ld %s(%s%s@David_Uton%s)
''' % (bold, red, end, bold, yellow, end))

# Extract files with password
def extractZip():
    with zipfile.ZipFile(fileZip) as file:
        try:
            statusPassword.status("%s" % password)            
            file.setpassword(pwd = bytes(password, 'utf-8'))
            file.extractall()
            showFinalTime = datetime.now()
            print("%s[%s!%s] %sDNI Found!:%s %s%s - The files have been extracted." % (bold, green, end, bold, end, dniNum, letter[rest]))
            print("%s[%s+%s] Cracking completed: %sh" % (bold, blue, end, showFinalTime.strftime("%d/%m/%Y %H:%M")))
            print("%s[%s*%s] Press %sControl + C%s to exit" % (bold, yellow, end, bold, end))
            file.close()
        except:
            pass

def handler(sig, frame):
    log.failure("Exit...")
    sys.exit(0)
 
signal.signal(signal.SIGINT, handler)

# Show results
if len(sys.argv) > 1:
    logotype()
    fileZip = sys.argv[1]
    print("%s[%s+%s] Start cracking: %sh" % (bold, blue, end, showTime.strftime("%d/%m/%Y %H:%M")))
    statusPassword = log.progress("Password testing:")

    for dniNum in range(10000000,99999999): 
        rest = dniNum % 23 
        password = "%s%s" % (dniNum, letter[rest]) 
        extractZip() 
else:
    print("%s[%s!%s] Error, missing .zip file." % (bold, red, end))