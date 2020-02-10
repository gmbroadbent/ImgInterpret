import sys
from colorama import Fore
import os


def _help():
    print(Fore.BLUE + "Help Menu" + Fore.RESET)
    print("\\ImgInterpret> python main.py [-h] [-t] [-g] [-a] <path>\n")

    print(Fore.LIGHTCYAN_EX + "-h" + Fore.RESET + " - Display help menu")
    print(Fore.LIGHTCYAN_EX + "-t" + Fore.RESET + " - Image background will be transparent")
    print(Fore.LIGHTCYAN_EX + "-g" + Fore.RESET + " - Grid lines included in image")
    print(Fore.LIGHTCYAN_EX + "-a" + Fore.RESET + " - Represents repeated RGB values with modified a Alpha value")
    print()
    print(Fore.LIGHTCYAN_EX + "<path>" + Fore.RESET + " - The path to image file to use.    (eg: bin/img.png)")

    print("\n")
    print(Fore.YELLOW + "Note" + Fore.RESET)
    print("This program is currently only capable of working with .png and .jpg formatted images")
    print("Results of images with over 10,000 pixels will render and react very slowly")


def _options(arg):
    pass


def _check_path(path):
    print("Checking path:  ", end='')

    if os.path.isfile(path):
        print(Fore.LIGHTGREEN_EX + path + Fore.RESET)
        if _check_format(path):
            return True
        else:
            return False
    else:
        print(Fore.RED + path + Fore.RESET)
        return False


def _check_format(path):

    print("\tChecking format:  ", end='')
    _, ext = os.path.splitext(path)

    if len(ext) < 2:
        print(len(ext))
        print(Fore.RED + "No extension" + Fore.RESET)
        return False

    if ext.upper() == '.JPG' or ext.upper() == '.PNG':
        print(Fore.LIGHTGREEN_EX + ext + Fore.RESET)
        return True

    else:
        print(Fore.RED + ext + Fore.RESET)
        return False
