import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # a
    f = open("./data/locationData.csv", "r")

    locData = []

    for line in f:  # f is "iterable"

        if "id" in line:  # Skip first line
            continue

        row = line.split(" ")

        numbers = []
        for val in row:
            numbers.append(float(val.strip()))

        locData.append(numbers)


    locDataNP = np.loadtxt("./data/locationData.csv")

    if np.any([locData, locDataNP]):
        print("same")



