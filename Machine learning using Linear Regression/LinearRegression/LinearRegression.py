import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

training = pd.read_csv('E:/train.csv')

x_training = training['x']
y_training = training['y']

x_training = np.array(x_training)
y_training = np.array(y_training)


# print(x_training, " ", y_training)


def finda(m, alpha, y_training, x_training):
    count = 0
    a0 = 0
    a1 = 0
    while count < 90000:
        y = a0 + a1 * x_training
        error = y - y_training
        mean_square_error = (1 / m) * (np.sum(error) ** 2)
        a0 = a0 - (alpha * (2 / m) * np.sum(error))
        a1 = a1 - (alpha * (2 / m) * np.sum(error*x_training))
        count += 1
        print(mean_square_error, " :", "y = ", a0, " + ", a1, "x")


finda(98, 0.0001, y_training, x_training)

plt.scatter(x_training, y_training)
plt.rcParams["scatter.marker"] = ','
