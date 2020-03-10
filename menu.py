from pynput.keyboard import Key, Listener
from colorama import Fore, Style, init
import sys
import os

init()    # Initiates colorama

stop = False
args = {"g": False,
        "h": False,
        "t": False,
        "a": False}

def _main():
    global args

    # args = {"g": False,
    #             "h": False,
    #             "t": False,
    #             "a": False}

    print("G - Include grid lines")
    print("H - HSV representation")
    print("T - Transparent background")
    print("A - Cumulative data-points")
    print()
    print("Press <ENTER> to continue to input path")
    print("Or <ESC> to exit")
    print()

    _print_args()

    l = Listener(on_press=_listen_press, suppress=True)
    l.start()
    l.join()

    if stop:
        exit(1)

    print("\n"*5)

    print("Enter image path as: ")
    print("Global: C:\...\img.jpg")
    print("OR")
    print("Local:  ...\img.png")
    print()
    print("Note:    Extensions must be included")
    print("To exit: X")
    print()
    print()

    while True:
        path_in = input("Path:\t").upper()

        if path_in == "X":
            exit(1)

        if _check_path(path_in):
            if _check_ext(path_in):
                break
            else:
                print("Invalid or Unusable extension\n")
        else:
            print("No such path exists\n")

    args_out = [args['g'], args['h'], args['t'], args['a'], path_in]
    print(args_out)
    # return args_out
    return args['g'], args['h'], args['t'], args['a'], path_in


def _print_args():
    global args

    sys.stdout.write("\b"*7)
    sys.stdout.flush()

    for arg, val in args.items():
        e = " "
        if arg == "a":
            e = ""

        if val:
            print(Fore.LIGHTGREEN_EX + arg.upper() + Fore.RESET, end=e)
        else:
            print(Fore.LIGHTRED_EX + arg.upper() + Fore.RESET, end=e)


def _check_path(path):
    if os.path.isfile(path):
        return True
    return False


def _check_ext(path):
    _, ext = os.path.splitext(path)

    if ext.upper() == '.JPG' or ext.upper() == '.PNG':
        return True

    return False


def _listen_press(key):
    global args
    global stop

    # print(key, str(key), key == str(key))
    str_key = str(key).replace("'", "")

    if key == Key.enter:
        return False

    if key == Key.esc:
        stop = True
        return False

    if str_key in args:
        args[str_key] = not args[str_key]
        _print_args()



# _main()
