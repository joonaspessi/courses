import numpy as np
from scipy.io import loadmat
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


if __name__ == "__main__":
    data = loadmat("data/arcene.mat")
    X_train = data["X_train"]
    X_test = data["X_test"]
    y_train = data["y_train"].ravel()
    y_test = data["y_test"].ravel()

    # Instantiate RFECV with logistic regression classifier
    rfe = RFECV(LogisticRegression(), step=50, verbose=True)

    # Fit training data, use default 3-fold cross validation
    rfe.fit(X_train, y_train)
    rfe.support_

    # Errors for different number of features
    plt.plot(range(0, 10001, 50), rfe.grid_scores_)
    plt.show()

    # Compute accuracy against test set
    y_pred = rfe.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print("accuracy:", score * 100, "%")