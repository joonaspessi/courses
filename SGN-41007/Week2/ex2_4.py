from scipy.io import loadmat
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mat = loadmat("./data/twoClassData.mat")
    print(mat.keys())
    X = mat["X"]
    y = mat["y"].ravel()

    XNeg = X[y == 0, :]
    XPos = X[y == 1, :]
    plt.plot(XNeg[:, 0], XNeg[:, 1], "ro")
    plt.plot(XPos[:, 0], XPos[:, 1], "bo")
    plt.show()
