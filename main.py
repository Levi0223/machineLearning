# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import kNN
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import array


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def f(a, /, b, c, d, e, *, f):
    print(a, b, c, d, e, f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('world')
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()
    str

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
