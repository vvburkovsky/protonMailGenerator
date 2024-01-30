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
            code = str(re.findall(r'(\d{6})', (str(value))))
            code = code.replace('[', '')
            code = code.replace(']', '')
            code = code.replace('\'', '')
            return code
    finally:
        user32.CloseClipboard()

def get_temporary_mail():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            mails = [
                "@dropmail.me",
                "@10mail.org",
                "@yomail.info",
                "@emltmp.com",
                "@emlpro.com",
                "@emlhub.com",
                "@zeroe.ml",
                "@laste.ml",
                "@freeml.net",
                "@10mail.tk",
                "@minimail.gq",
                "@flymail.tk",
                "@spymail.one",
                "@10mail.xyz"
            ]
            for mail in mails:
                if mail in str(value):
                    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
                    return str(match.group(0))
            return False
    finally:
        user32.CloseClipboard()

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

def open_browser():
    webbrowser.open('https://google.com')

    time.sleep(5)
    pyautogui.keyDown('ctrlleft'); pyautogui.keyDown('shift'); pyautogui.typewrite('p'); pyautogui.keyUp('ctrlleft'); pyautogui.keyUp('shift')
    pyautogui.typewrite('https://account.proton.me/signup?plan=free\n')
    time.sleep(5)

    # Username
    _username_=randomize('-s',5)+randomize('-s',5)+randomize('-s',5)
    pyautogui.typewrite(_username_ + '\t\t')
    print("Username:" + _username_)

    # Password
    _password_=randomize('-p',16)
    pyautogui.typewrite(_password_+'\t'+_password_+'\t')
    print("Password:" + _password_)

    #Repeate Password
    pyautogui.typewrite(_password_+'\t')
    time.sleep(5)

    pyautogui.typewrite('\n')
    time.sleep(5)
    pyautogui.typewrite('\t\t\t\n')

    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')

    time.sleep(5)
    pyautogui.typewrite('https://dropmail.me/en/\n')

    return _username_, _password_

def get_and_paste_mail():
    newMail = None
    while True:
        if not newMail:
            pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
            time.sleep(5)
        pyautogui.typewrite(28 * '\t')
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.press('down')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
        newMail = get_temporary_mail()

        if newMail:
            print("10 min mail: " + newMail)
            break
    paste_and_check()
                
def paste_and_check():
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    time.sleep(1)
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('v'); pyautogui.keyUp('ctrlleft')
    pyautogui.press('backspace')
    pyautogui.typewrite('\n')

    time.sleep(5)

    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    time.sleep(1)

    for i in range(0, 10):
        pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
        code = getClip6digit()
        if len(code) == 6:
            print("Code found")
            print(code)
            pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
            time.sleep(2)
            pyautogui.typewrite(code + '\n')
            time.sleep(30)
            pyautogui.typewrite('\n')
            time.sleep(10)
            pyautogui.typewrite('\t\t\t\n')
            time.sleep(5)
            pyautogui.typewrite('\t\n')
            time.sleep(5)
            pyautogui.typewrite('\t\n')
            break
        time.sleep(2)

        if i == 9:
            print("No code found")
            pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
            time.sleep(1)
            pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft'); pyautogui.keyDown('backspace'); pyautogui.keyUp('backspace')
            time.sleep(1)
            pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
            time.sleep(1)
            get_and_paste_mail()

def main():
    try:
        username, password = open_browser()
        logfile = open("accLog.txt", "a")
        logfile.write(username + "@proton.me:" + password + "\n")
        get_and_paste_mail()
        logfile.close()
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()


