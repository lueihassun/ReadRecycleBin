import os
import winreg
from winreg import *


# SID in Nutzernamen umwandeln
def sid2user(sid):
    try:
        access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        key = winreg.OpenKey(access_registry,
                             "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList" + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid


# Papierkorb-Verzeichnis finden
def return_dir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycle_dir in dirs:
        if os.path.isdir(recycle_dir):
            return recycle_dir

    return None


# Gelöschte Dateien für jeden Nutzer anzeigen
def find_recycled(recycle_dir):
    dir_list = os.listdir(recycle_dir)
    unrectext = ''
    for sid in dir_list:
        files = os.listdir(recycle_dir + sid)
        user = sid2user(sid)
        unrectext += '\n\n[*] Listing Files for User: ' + str(user)
        for file in files:
            unrectext += '\n [+] Found Files: ' + str(file)

    return unrectext


def main():
    recycled_dir = return_dir()
    result = find_recycled(recycled_dir)
    # Ergebnisse anzeigen.
    print(result)


if __name__ == '__main__':
    main()

