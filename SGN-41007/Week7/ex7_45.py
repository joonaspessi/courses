import numpy as np
from scipy.io import loadmat
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
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

    # ex5
    c_range = np.linspace(1e-5, 100, num=10)
    for C in c_range:
        clf = LogisticRegression(penalty="l1", C=C)
        scores = cross_val_score(clf, X_train, y_train, cv=10)
        print("C: %.5f" % C)
        print("---------")
        print("CV Accuracy (10-fold): %.2f +- %.2f" % (np.mean(scores), np.std(scores)))

        model = LogisticRegression(penalty="l1", C=C)
        model.fit(X_train, y_train)

        a = np.where(model.coef_[0] > 1e-5)
        print("Selected coefficients: %d/%d" % (len(a[0]), len(model.coef_[0])))

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_train, y_pred)
        print("Test Accuracy: %.2f" % accuracy)
