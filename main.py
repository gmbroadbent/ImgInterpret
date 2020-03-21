try:
    import time
    # import pyttsx3
    import inspect
    import sys
    import os
    import math
    import numpy as np
    from datetime import datetime
    from matplotlib import pyplot as plt
    from matplotlib import colors as m_colors
    from colorama import Fore, Style, init
    from mpl_toolkits.mplot3d import axes3d, Axes3D
    from pynput.keyboard import Key, Listener
    import cv2
    import args
    import menu
except ModuleNotFoundError:
    print("ERROR:\n\tREQUIRED MODULES NOT FOUND")

    _ = input("\nPress enter to end")
    exit(-1)

# global transparent_img
# global grid
global arg_vals

init()    # Initiates colorama




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


def _write(path='bin\\img_small.png'):
    out_string = ""

    ext = os.path.splitext(path)[1].upper()[1:]

    matrix = plt.imread(path)
    if ext == "PNG":
        matrix *= 255    # float vals 0-255
        matrix = matrix.astype(int)    # int vals 0-255

    #try:
    #    if ext == "PNG":
    #        matrix = plt.imread(path)    # float vals 0-1
    #        matrix *= 255    # float vals 0-255
    #        matrix = matrix.astype(int)    # int vals 0-255
    #    else:
    #        if ext == "JPG":
    #            mat_in = plt.imread(path)  # float vals 0-255
    #except ValueError:
    #    print(Fore.RED + "\nERROR:\n\tIssue reading file" + Fore.RESET)
    #    print("\tFile may not be suitable for use")
    #    exit(-1)
    #except:
    #    print(Fore.RED + "ERROR:\n\tCOULD NOT READ FILE" + Fore.RESET)
    #    exit(-1)
            

    m_0 = matrix.shape[0]
    m_1 = matrix.shape[1]

    try:
        f_name = os.path.basename(path)
        name, ext = os.path.splitext(f_name)
        new_fname = (name + "[" + ext[1:] + "].txt").upper()
        out_path = "BIN\\" + new_fname
    except:
        print(Fore.RED + "ERROR:\n\tCOULD NOT GENERATE FILE NAME" + Fore.RESET)
        exit(-1)
    

    pixels = m_0*m_1
    num_len = len(str(pixels))
    back = (2* num_len)+1
    

    print("\n\n")

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):

            cur_pix = (i*m_0) + j + 1
            sys.stdout.write("\b"*back)
            sys.stdout.write('{val:0{width}}/{val1:0{width}}'.format(val=cur_pix, width=num_len, val1=pixels))
            sys.stdout.flush()

            # print("[", end='')
            # print(Fore.RED + '{0:03d}'.format(matrix[i][j][0]), end=' ')
            # print(Fore.GREEN + '{0:03d}'.format(matrix[i][j][1]), end=' ')
            # print(Fore.BLUE + '{0:03d}'.format(matrix[i][j][2]), end='')
            # print(Style.RESET_ALL + ']', end='\t')

            # print('{0:03d}'.format(matrix[i][j][0]), end='.')
            # print('{0:03d}'.format(matrix[i][j][1]), end='.')
            # print('{0:03d}'.format(matrix[i][j][2]), end='    ')

            # print('{0:03d}'.format(matrix[i][j][0]), end='.')
            # print('{0:03d}'.format(matrix[i][j][1]), end='.')
            # print('{0:03d}'.format(matrix[i][j][2]), end='  ')

            r = '{0:03d}'.format(matrix[i][j][0])
            g = '{0:03d}'.format(matrix[i][j][0])
            b = '{0:03d}'.format(matrix[i][j][0])
			
            # out_string = out_string + '{0:03d}'.format(matrix[i][j][0]
            out_string = out_string + r
            out_string = out_string + "."
            out_string = out_string + g
            out_string = out_string + '.'
            out_string = out_string + b
			
            if j < matrix.shape[1]:
                out_string = out_string + "    "

        # print()
        out_string = out_string + '\n'

    print("\n\n")

    try:
        with open(out_path, 'w') as file:
            try:
                file.write(out_string[:-1])
                print("Data written to " + out_path)
            except:
                print(Fore.RED + "ERROR:\n\tCOULD NOT WRITE TO FILE" + Fore.RESET)
                exit(-1)
    except:
        print(Fore.RED + "ERROR:\n\tCOULD NOT OPEN FILE" + Fore.RESET)
        exit(-1)
	
    # print(out_string)


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


def _plot_hsv(matrix):
    # _update()

    # print(matrix)

    global arg_vals

    hist = np.zeros([180], dtype=float)

    print("Fetching values...", end='    ')


    for col in matrix:
        for pix in col:
            if pix[1] > 5 and pix[2] > 5:    # Prevents use of absolute black or white
                hist[pix[0]] += 1

    SF = 1000/np.amax(hist)

    for i in range(len(hist)):
        hist[i] *= SF

    print(Fore.GREEN + "Done" + Fore.RESET)

    print("Settings points...", end='    ')

    points = np.zeros([180, 2, 2], dtype=float)

    for i in range(len(hist)):
        theta = i*2

        if theta % 90 == 0:    # Theta = [0, 90, 180, 270]
            if theta == 0:
                points[i, 1] = [hist[i], 0]
            else:
                if theta == 90:
                    points[i, 1] = [0, hist[i]]
                else:
                    if theta == 180:
                        points[i, 1] = [-hist[i], 0]
                    else:
                        if theta == 270:
                            points[i, 1] = [0, -hist[i]]
                        else:
                            print(Fore.RED + "\nERROR Setting point" + Fore.RESET)
                            print("Theta: {}\nValue: {}".format(theta, hist[i]))
                            exit(-1)
        else:
            r = theta*(math.pi/180)    # Convert to radians
            if theta < 90:
                points[i, 1] = [(math.cos(r) * hist[i]), (math.sin(r) * hist[i])]
            else:
                if theta < 180:
                    r = math.pi-r
                    points[i, 1] = [(-1 * math.cos(r) * hist[i]), (math.sin(r) * hist[i])]
                else:
                    if theta < 270:
                        r = r-math.pi
                        points[i, 1] = [(-1 * math.cos(r) * hist[i]), (-1 * math.sin(r) * hist[i])]
                    else:
                        r = r-(2*math.pi)
                        points[i, 1] = [(math.cos(r) * hist[i]), (-1 * math.sin(r) * hist[i])]


        # print("{0:03d}\t{1}".format(i, hist[i]))
        # print("{}\t{}".format(i, hist[i]))

    print(Fore.GREEN + "Done" + Fore.RESET)

    _plot_2d(points)

    # for i in range(len(points)):
        # print("{0:03d}\t{1:04d} x {1:04d}".format(i*2, int(points[i, 1, 0]), int(points[i, 1, 1])))
        # print("{0:03d}\t{1}".format(i*2, points[i, 1]))
        # print(math.hypot(points[i, 1, 0], points[i, 1, 1]) > 1000)



def _plot_2d(vals):

    global arg_vals


    # fig = plt.figure()
    # ax = Axes3D(fig)

    x = np.zeros([2], dtype=float)
    y = np.zeros([2], dtype=float)

    c = plt.Circle((0, 0), 1000, fill=False)

    for i in range(len(vals)):
        x[0] = vals[i, 0, 0]
        x[0] = vals[i, 1, 0]

        y[0] = vals[i, 0, 1]
        y[0] = vals[i, 1, 1]

        hsv = np.array([(i/180), 0.5, 0.5], dtype=float)
        rgb = m_colors.hsv_to_rgb(hsv)

        plt.plot(x, y, c=rgb)

    axes = plt.gca()

    axes.add_artist(c)

    axes.set_xlim([-1010, 1010])
    axes.set_ylim([-1010, 1010])

    l = Listener(on_press=_listen_press)
    l.start()
    print("\n"*5)
    print("-"*30)
    print("\nSave Figure: " + Fore.BLUE + "<SPACE>" + Fore.RESET)
    print("Exit: " + Fore.BLUE + "<ESC>\n" + Fore.RESET)
    print("-"*30)
    print()

    if not arg_vals["g"]:
        axes.set_axis_off()

    plt.show()


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


def _work_hsv(path):
    # _update()

    print("Reading & Formatting file...", end='    ')

    try:
        mat_in = cv2.imread(path, cv2.IMREAD_COLOR)  # imports image as BGR
    except:
        print(Fore.RED + "\nERROR:\n\tIssue reading file" + Fore.RESET)
        print("\tFile may not be suitable for use")
        exit(-1)

    try:
        matrix = cv2.cvtColor(mat_in, cv2.COLOR_BGR2HSV)    # Convert BGR to HSV
    except:
        print(Fore.RED + "\nERROR:\n\tIssue converting data" + Fore.RESET)
        exit(-1)

    print(Fore.GREEN + "Done" + Fore.RESET)

    _plot_hsv(matrix)


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

    global arg_vals

    if arg_vals["w"]:
        _write(path)
    else:
        if arg_vals["h"]:
            # time.sleep(2.5)
            _work_hsv(path)
        else:
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
                "h": False,
                "t": False,
                "a": False,
                "w": False,
                "?": False}

    print("\n"*10)

    if len(sys.argv) < 2:
        menu_args = menu._main()
        arg_vals['g'] = menu_args[0]
        arg_vals['h'] = menu_args[1]
        arg_vals['t'] = menu_args[2]
        arg_vals['a'] = menu_args[3]
        arg_vals['w'] = menu_args[4]
        path = menu_args[5]
        
        try:
            _main(path)
        except ImportError:
            print(Fore.RED + "ERROR:\n\tREQUIRED MODULES MISSING" + Fore.RESET)
            exit(-1)
        #except:
            #print(Fore.RED + "ERROR:\n\tUNKNOWN FAILURE" + Fore.RESET)
            #exit(-1)

    for arg in sys.argv[1:]:
        if arg[0] == '-':
            if len(arg) == 2:
                if arg[1] == '?':
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
                                if arg[1] == "h":
                                    arg_vals["h"] = True
                                else:
                                    if arg[1] == "w":
                                        arg_vals["w"] = True
                                    else:
                                        print(Fore.RED + arg + Fore.RESET, end='    ')
                                        print("Invalid switch    " + Fore.CYAN + "(-? for help)" + Fore.RESET)
            else:
                print(Fore.RED + arg + Fore.RESET, end='    ')
                print("Invalid argument    " + Fore.CYAN + "(-? for help)" + Fore.RESET)
        else:
            if args._check_path(arg):
                try:
                    _main(arg)
                    exit(1)
                except ImportError:
                    print(Fore.RED + "ERROR:\n\tISSUE WITH REQUIRED MODULES" + Fore.RESET)
                    exit(-1)

    print("(-? for help)")
