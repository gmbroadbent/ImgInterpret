# import pyttsx3
import inspect
import sys
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
from colorama import Fore, Style, init
from mpl_toolkits.mplot3d import axes3d, Axes3D
from pynput.keyboard import Key, Listener
import args

# global transparent_img
# global grid
global arg_vals

init()    # Initiates pynput




def _update():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print(Fore.GREEN + '{}'.format(calframe[1][3]))
    print(Style.RESET_ALL)


def _plot_3d(x, y, z, a=0.25):
    # _update()

    # a=0.25

    global arg_vals

    print("Fetching colours...", end='    ')

    if arg_vals["a"]:
        colours = np.zeros([x.shape[0], 4], dtype=float)
        for i in range(colours.shape[0]):
            colours[i] = [float(x[i])/255, float(y[i])/255, float(z[i])/255, float(a[i])]
    else:
        colours = np.zeros([x.shape[0], 4], dtype=float)
        for i in range(colours.shape[0]):
            colours[i] = [(float(x[i])/255), (float(y[i])/255), (float(z[i])/255), 0.25]

    print(Fore.GREEN + "Done" + Fore.RESET)

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter(x, y, z, c=colours, marker=".")

    # if type(a).__name__ == float:
    #     ax.scatter(x, y, z, alpha=a, c=colours/255, marker=".")
    # else:
    #     print(a)
    #     for i in range(len(x)):
    #         ax.scatter(x[i], y[i], z[i], alpha=a[i], c=colours[i]/255, marker=".")

    ax.set_xlim(0, 255)
    ax.set_xlabel('R')

    ax.set_ylim(0, 255)
    ax.set_ylabel('G')

    ax.set_zlim(0, 255)
    ax.set_zlabel('B')

    # plt.savefig("bin\\RGB_Analysis.png", dpi=200)
    # with Listener(on_press=_listen_press) as listener:
    #     print("\nSave image: " + Fore.BLUE + "<SPACE>" + Fore.RESET)
    #     print("Exit: " + Fore.BLUE + "<ESC>\n" + Fore.RESET)
    #     plt.show()
    #     listener.join()

    l = Listener(on_press=_listen_press)
    l.start()

    print("\n"*5)
    print("-"*30)
    print("\nSave Figure: " + Fore.BLUE + "<SPACE>" + Fore.RESET)
    print("Exit: " + Fore.BLUE + "<ESC>\n" + Fore.RESET)
    if(len(x) > 10000):
        print(Fore.RED + "Caution: " + Fore.RESET)
        print("Large images (>10,000 pixels) take a while to render\n")
    print("-"*30)
    print()

    if not arg_vals["g"]:
        ax.set_axis_off()

    plt.show()
    # l.close()


def _test():
    path = 'bin\\img_small.png'
    # path = 'bin\\img_main.png'
    matrix = plt.imread(path)    # float vals 0-1
    matrix *= 255    # float vals 0-255
    matrix = matrix.astype(int)    # int vals 0-255

    print("\n\n")

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):

            # print("[", end='')
            # print(Fore.RED + '{0:03d}'.format(matrix[i][j][0]), end=' ')
            # print(Fore.GREEN + '{0:03d}'.format(matrix[i][j][1]), end=' ')
            # print(Fore.BLUE + '{0:03d}'.format(matrix[i][j][2]), end='')
            # print(Style.RESET_ALL + ']', end='\t')

            # print('{0:03d}'.format(matrix[i][j][0]), end='.')
            # print('{0:03d}'.format(matrix[i][j][1]), end='.')
            # print('{0:03d}'.format(matrix[i][j][2]), end='    ')

            print('{0:03d}'.format(matrix[i][j][0]), end='.')
            print('{0:03d}'.format(matrix[i][j][1]), end='.')
            print('{0:03d}'.format(matrix[i][j][2]), end='  ')

        print()

    print("\n\n")


def _plot(matrix):
    # _update()

    global arg_vals

    vals = np.zeros([3, matrix.shape[0]*matrix.shape[1]], dtype=int)

    pos = 0

    print("Fetching values...", end='    ')

    if arg_vals["a"]:
        RGBs = {}
        # new_range = 1-0.5
        max_val = 1
        r = []
        g = []
        b = []

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                val = "{}-{}-{}".format(matrix[i][j][0], matrix[i][j][1], matrix[i][j][2])
                if val in RGBs:
                    RGBs[val] += 1
                    if RGBs[val] > max_val:
                        max_val = RGBs[val]
                else:
                    RGBs[val] = 1
                    r.append(int(matrix[i][j][0]))
                    g.append(int(matrix[i][j][1]))
                    b.append(int(matrix[i][j][2]))

        print(Fore.GREEN + "Done" + Fore.RESET)
        print("Standardising alphas...", end='    ')

        vals = np.zeros([3, len(RGBs)], dtype=int)

        alphas = np.array(list(RGBs.values()))
        alphas = ((alphas * (1-0.25)) / max_val) + 0.25    # Standardise values [0.25-1.0]

        print(Fore.GREEN + "Done" + Fore.RESET)

        _plot_3d(np.array(r, dtype=int), np.array(g, dtype=int), np.array(b, dtype=int), alphas)
        # _plot_3d(vals[0], vals[1], vals[2], alphas)

        # new_val = ((oldVal-oldMin) * (new_max-new_min)) / (oldMax-oldMin)
        # new_val += newMin

        exit(1)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):

            vals[0][pos] = matrix[i][j][0]
            vals[1][pos] = matrix[i][j][1]
            vals[2][pos] = matrix[i][j][2]

            pos += 1

        # print("[ {} / {} ]".format(i, matrix.shape[0]))

    print(Fore.GREEN + "Done" + Fore.RESET)

    _plot_3d(vals[0], vals[1], vals[2])


def _plot_png(path):
    # _update()

    print("Reading & Formatting file...", end='    ')

    try:
        mat_in = plt.imread(path)  # float vals 0-1
    except ValueError:
        print(Fore.RED + "\nERROR:\n\tIssue reading file" + Fore.RESET)
        print("\tFile may not be suitable for use")
        exit(-1)
    matrix = mat_in * 255  # float vals 0-225
    matrix = matrix.astype(int)  # int vals 0-225

    print(Fore.GREEN + "Done" + Fore.RESET)

    _plot(matrix)


def _plot_jpg(path):
    # _update()

    print("Reading & Formatting file...", end='    ')

    try:
        mat_in = plt.imread(path)  # float vals 0-255
    except ValueError:
        print(Fore.RED + "\nERROR:\n\tIssue reading file" + Fore.RESET)
        print("\tFile may not be suitable for use")
        exit(-1)
    matrix = mat_in  # float vals 0-255
    matrix = matrix.astype(int)  # int vals 0-255

    print(Fore.GREEN + "Done" + Fore.RESET)

    _plot(matrix)


def _listen_press(key):
    # global saved
    # print("Key Pressed: " + Fore.BLUE + "{}".format(key) + Style.RESET_ALL)

    global arg_vals

    if key == Key.esc:
        plt.close()
        return False
    else:
        if key == Key.space:
            print("Naming...", end='    ')
            today = datetime.today().strftime("%y%M%d")
            now = datetime.now().strftime("%H%M%S")
            path = "bin\\{}_{}.png".format(today, now)
            print(Fore.GREEN + "Done" + Fore.RESET)

            try:
                print("Saving...", end='    ')
                plt.savefig(path, dpi=400, transparent=arg_vals["t"])
                # saved += 1
                print(Fore.GREEN + "Image saved: {}".format(path) + Fore.RESET)
            except:
                print(Fore.RED + "Failed to save image" + Fore.RESET)


def _main(path):

    print("\n")

    extension = path.split(".")[-1].upper()

    if extension == "PNG":
        _plot_png(path)
    else:
        if extension == "JPG":
            _plot_jpg(path)
        else:
            print(Fore.RED + "ERROR:\n\tUNUSABLE FORMAT" + Fore.RESET)
            exit(-1)


if __name__ == "__main__":

    # transparent_img = False
    # grid = False

    arg_vals = {"g": False,
                "t": False,
                "a": False}

    print("\n"*10)

    if len(sys.argv) < 2:
        args._help()
        exit(1)

    for arg in sys.argv[1:]:
        if arg[0] == '-':
            if len(arg) == 2:
                if arg[1] == 'h':
                    args._help()
                else:
                    if arg[1] == 't':
                        arg_vals["t"] = True
                    else:
                        if arg[1] == 'g':
                            arg_vals["g"] = True
                        else:
                            if arg[1] == 'a':
                                arg_vals["a"] = True
                            else:
                                print(Fore.RED + arg + Fore.RESET, end='    ')
                                print("Invalid switch    " + Fore.CYAN + "(-h for help)" + Fore.RESET)
            else:
                print(Fore.RED + arg + Fore.RESET, end='    ')
                print("Invalid argument    " + Fore.CYAN + "(-h for help)" + Fore.RESET)
        else:
            if args._check_path(arg):
                _main(arg)
                exit(1)
                # else:
                    # exit(1)
            # exit(1)
