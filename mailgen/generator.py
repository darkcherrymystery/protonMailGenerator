#! python3
#Michi4
from PIL import Image
import pyautogui
import sys
import time
import random
import string
import webbrowser
import ctypes
import re

CF_TEXT = 1

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p

def getClip6digit():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            return str(re.findall(r'(\d{6})', (str(value))))
    finally:
        user32.CloseClipboard()

def getMail():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            # if "@dropmail.me" in str(value)  or "@10mail.org"  in str(value)  or "@emlpro.com" in str(value) or "@emltmp.com" in str(value): # commented to disable manual filters
            if True: # accept eny email hosting here because new email checking function is used later
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
                return str(match.group(0))
            return False
    finally:
        user32.CloseClipboard()
webbrowser.open('https://google.com')

time.sleep(5)
pyautogui.keyDown('ctrlleft'); pyautogui.keyDown('shift'); pyautogui.typewrite('p'); pyautogui.keyUp('ctrlleft'); pyautogui.keyUp('shift')
pyautogui.typewrite('https://account.proton.me/signup?plan=free\n')
time.sleep(5) 

def randomize(
                _option_,
                _length_
            ):

    if _length_ > 0 :

        # Options:
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_='1234567890'
        elif _option_ == '-m':
            string._characters_='JFMASOND'

        if _option_ == '-d':
            _generated_info_=random.randint(1,28)
        elif _option_ == '-y':
            _generated_info_=random.randint(1950,2000)
        else:
            _generated_info_=''
            for _counter_ in range(0,_length_) :
                _generated_info_= _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        return 'error'

def getVerificationCode(): # switches to dropmail tab, gets a verification code and returns it

    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    time.sleep(1)

    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')

    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    time.sleep(5)

    code = str(getClip6digit())

    return code

# Username
_username_=randomize('-s',5)+randomize('-s',5)+randomize('-s',5)
pyautogui.typewrite(_username_ + '\t\t\t') #added \t
print("Username:" + _username_)

# Password
_password_=randomize('-p',16)
pyautogui.typewrite(_password_+'\t'+_password_+'\t')
print("Password:" + _password_)

pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t') #removed \n

pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')

time.sleep(10)
pyautogui.typewrite('https://dropmail.me/\n')


pyautogui.keyDown('shift');pyautogui.keyDown('down'); pyautogui.keyUp('down'); pyautogui.keyUp('shift')
time.sleep(10)

newMail = True
while True:
    if not newMail:
        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
        time.sleep(5)
    pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')#28
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('down')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
    newMail = getMail()
    if newMail:
        print("10 min mail: " + newMail)
        break

pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
pyautogui.typewrite('\t\t'); # added \t
time.sleep(1)
pyautogui.typewrite(newMail) # uncommented
#pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('v'); pyautogui.keyUp('ctrlleft') # commented
#pyautogui.press('backspace') # commented
pyautogui.typewrite('\n\n') # added \n

time.sleep(10)

while True:

    verification_code = getVerificationCode()

    if str(verification_code) != "[]":

        break

    else:  

        pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
        time.sleep(1)

        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
        time.sleep(5)
        pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')#28
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.press('down')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
        newMail = getMail()

        pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
        time.sleep(1)

        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('v'); pyautogui.keyUp('ctrlleft')

        pyautogui.typewrite('\n')
        time.sleep(20) # sometimes emails are sent with a delay, 20 sec is enough


        # This "While True" block generates new emails and
        #   checks them until Proton accepts

        # If email is accepted, verification_code will contain a valid verification code
        # If not, verification_code will contain "[]"


pyautogui.typewrite(str(getClip6digit()) + '\n')


time.sleep(5)
pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t\t\n')
time.sleep(1)
pyautogui.typewrite('\n') # removed \t

print(_username_+"@proton.me:" + _password_)

logfile = open("accLog.txt", "a")
logfile.write(_username_ + "@proton.me:" + _password_ + "\n")
logfile.close()



# CHAPTCHA
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')

#pyautogui.typewrite('\n')