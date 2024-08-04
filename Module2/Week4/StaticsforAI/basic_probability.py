import numpy as np


def compute_mean(X):
    return np.mean(X)


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print(X)
    if (size % 2 == 0):
        return (X[size // 2 - 1] + X[size // 2]) / 2
    else:
        return X[size // 2]


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    variance = sum((i - mean)**2 for i in X) / len(X)
    return np.sqrt(variance)


def compute_correlation_coefficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0
    numerator = N * X.dot(Y) - sum(X) * sum(Y)
    denominator = np.sqrt(N * sum(X ** 2) - sum(X) ** 2) * \
        np.sqrt(N * sum(Y ** 2) - sum(Y) ** 2)
    return np.round(numerator / denominator, 2)


X1 = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print('Mean: ', compute_mean(X1))

X2 = [1, 5, 4, 4, 9, 13]
print('Median: ', compute_median(X2))

X3 = [171, 176, 155, 167, 169, 182]
print(compute_std(X3))

X4 = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y4 = np.asarray([4, 25, 121, 36, 16, 225, 81])
print('Correlation: ', compute_correlation_coefficient(X4, Y4))
