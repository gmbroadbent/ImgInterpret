import os
import time
import numpy as np
from matplotlib import pyplot as plt
from colorama import Fore


def _average(path):
    t0 = time.time()
    print("Processing file: {}".format(path), end='    ')

    average = np.zeros([3], dtype=float)
    alpha = False
    
    img = plt.imread(path)
    res = img.shape[0] * img.shape[1]

    if len(img[0][0]) > 3:
        alpha = True
        res = 0
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if alpha:
                if img[i][j][3] > 0:
                    average += img[i][j][0:3]
                    res += 1
            else:
                average += img[i][j][0:3]
    
    average /= res

    t1 = time.time()

    print("Done in {} secs".format(t1-t0))
    
    return average


def _progression(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            _, ext = os.path.splitext(file)

            if ext.upper() == ".PNG" or ext.upper() == ".JPG":
                print(Fore.GREEN + "{}{}".format(path, file) + Fore.RESET)
            else:
                print("{}{}".format(path, file))


if __name__ == "__main__":
    _ = _average("bin/littlecato.png")
