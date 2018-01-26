import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    x = np.load('./data/x.npy')
    y = np.load('./data/y.npy')

    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]

    print(m, c)

    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(x, m*x + c, 'r', label='Fitted line')
    plt.legend()
    plt.show()
