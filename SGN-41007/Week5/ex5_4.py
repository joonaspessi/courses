from skimage.feature import local_binary_pattern
from skimage import io
from os.path import join, abspath
from os import walk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt
import numpy as np
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Parameters for local binary pattern LBP
METHOD = "default"
radius = 2
n_points = 8 * radius


def absolute_file_paths(directories):
    for directory in directories:
        for dirpath, _, filenames in walk(directory):
            for f in filenames:
                yield abspath(join(dirpath, f))


def get_histogram(imgPath):
    image = io.imread(imgPath)
    lbp = local_binary_pattern(image, n_points, radius, METHOD)
    n_bins = int(lbp.max() + 1)
    (hist, _) = np.histogram(lbp.ravel(), density=False, bins=n_bins)
    return hist


def plot_image_with_histogram(sample_images, title):
    # Randomly pick three images
    images = random.sample(sample_images, 3)
    lbps = []
    for img in images:
        lbps.append(local_binary_pattern(img, n_points, radius, METHOD))

    fig, (ax_img, ax_lbp) = plt.subplots(nrows=2, ncols=3, figsize=(9, 6))
    fig.suptitle(title, fontsize=16)
    plt.gray()

    for idx, (axi, axl) in enumerate(zip(ax_img, ax_lbp)):
        axi.imshow(images[idx])
        axl.imshow(lbps[idx])

    plt.show()


if __name__ == "__main__":
    X = []
    Y = []
    images1 = []
    images2 = []

    imageFileNamesClass1 = absolute_file_paths([os.path.join(dir_path, "data", "GTSRB_subset", "class1")])
    for imgPath in imageFileNamesClass1:
        image = io.imread(imgPath)
        images1.append(image)
        X.append(get_histogram(imgPath))
        Y.append(0)

    imageFileNamesClass2 = absolute_file_paths([os.path.join(dir_path, "data", "GTSRB_subset", "class2")])
    for imgPath in imageFileNamesClass2:
        image = io.imread(imgPath)
        images2.append(image)
        X.append(get_histogram(imgPath))
        Y.append(1)

    # plot_image_with_histogram(images1, "Sample of Class 1 images and LBS")
    # plot_image_with_histogram(images2, "Sample of Class 2 images and LBS")

    Xnorm = Normalizer().transform(X)
    X_train, X_test, y_train, y_test = train_test_split(Xnorm, Y, test_size=0.80)

    C_range = np.linspace(10e-5,10e0, num=10)
    clf_list = [LogisticRegression, SVC]

    bestScore = 0
    bestClf = ""

    # todo use GridSearchCV
    for Clf in clf_list:
        clf = Clf()
        name = Clf.__name__
        for C in C_range:
            for penalty in ["l1", "l2"]:
                clf.C = C
                clf.penalty = penalty
                clf.fit(X_train, y_train)
                clf.foobar = "moi"
                y_pred = clf.predict(X_test)
                score = accuracy_score(y_test, y_pred)
                if score > bestScore:
                    bestScore = score
                    bestClf = name
                print("training", name, "with C:", C, "and penalty:", penalty, "SCORE:", score)

    print("Best classifier is:", bestClf, "with score of:", bestScore)
exit()
