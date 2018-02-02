from math import sqrt, pi
from numpy import log, exp, linspace
import matplotlib.pyplot as plt


def gaussian(x, mu, sigma):
    a = 1 / (sqrt(2 * pi) * sigma)
    b = exp(-pow(x - mu, 2) / (2 * pow(sigma, 2)))
    return a * b


def log_gaussian(x, mu, sigma):
    a = log(1 / (sqrt(2 * pi) * sigma))
    b = -pow(x - mu, 2) / (2 * pow(sigma, 2))
    return a + b


if __name__ == "__main__":
    x = linspace(-5, 5, num=1000)
    y1 = gaussian(x, 0, 1)
    y2 = log_gaussian(x, 0, 1)
    plt.plot(x, y1, 'r', label='gaussian')
    plt.plot(x, y2, 'b', label='log_gaussian')
    plt.show()

    f, axarr = plt.subplots(2)
    axarr[0].plot(x, y1, 'r', label='gaussian')
    axarr[1].plot(x, y2, 'b', label='log_gaussian')
    plt.show()

exit()