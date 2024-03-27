import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def freq(x, prob=True):
    unique_values, counts = np.unique(x, return_counts=True)
    if prob:
        probabilities = counts / len(x)
        return unique_values, probabilities
    else:
        return unique_values, counts


def freq2(x, y, prob=True):
    combined_data = np.column_stack((x, y))

    unique_combinations, counts = np.unique(combined_data, axis=0, return_counts=True)

    xi = unique_combinations[:, 0]
    yi = unique_combinations[:, 1]

    if prob:
        total_counts = np.sum(counts)
        probabilities = counts / total_counts
        return xi, yi, probabilities
    else:
        return xi, yi, counts


def entropy(x):
    _, probabilities = freq(x)
    h = -sum(p * math.log2(p) for p in probabilities if p != 0)
    return h


def ixy(x, y):
    hx = entropy(x)
    hy = entropy(y)
    hxy = entropy(list(zip(x, y)))
    ixy = hx + hy - hxy
    return ixy

def iyx(x, y):
    hx = entropy(x)
    hxy = entropy(list(zip(x, y)))
    iyx = hx - hxy
    return iyx


if __name__ == '__main__':
    print("a")
    df = pd.read_csv("zoo.csv")
    print(df["eggs"])
    print(df["type"])
    x = np.array([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    x2 = np.array(['a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd'])
    y2 = np.array([1, 2, 1, 2, 3, 4, 3, 3, 4, 4, 4])
    xi, pi = freq(x)
    print("Unikalne wartości xi:", xi)
    print("Estymowane prawdopodobieństwa pi:", pi)

    xi, ni = freq(x, prob=False)
    print("Unikalne wartości xi:", xi)
    print("Częstości ni:", ni)

    xi, yi, ni = freq2(x2, y2)
    print(xi)
    print(yi)
    print(ni)

    xi, yi, ni = freq2(x2, y2, False)
    print(xi)
    print(yi)
    print(ni)

    x = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    y = [10, 20, 20, 30, 30, 30, 40, 40, 40, 40, 50]

    h = entropy(x)
    print("Entropy h:", h)

    i = ixy(x, y)
    print("Information gain i:", i)

    mutual_info = iyx(x, y)
    print("Mutual information i(Y, X):", mutual_info)

# import pandas as pd
# import math
#
# # Wczytanie danych z pliku CSV
# data = pd.read_csv("zoo.csv")
#
# # Funkcja do obliczania entropii
# def entropy(labels):
#     n_labels = len(labels)
#     if n_labels <= 1:
#         return 0
#     counts = pd.Series(labels).value_counts() / n_labels
#     return -counts.dot(counts.apply(math.log, args=(2,)))
#
# # Funkcja do obliczania przyrostu informacji dla danego atrybutu
# def information_gain(data, attribute):
#     total_entropy = entropy(data['class_type'])
#     attribute_entropy = 0
#     for value in data[attribute].unique():
#         subset = data[data[attribute] == value]
#         attribute_entropy += len(subset) / len(data) * entropy(subset['class_type'])
#     return total_entropy - attribute_entropy
#
# # Wybór atrybutu z największym przyrostem informacji
# attributes = data.columns[:-1]  # Wszystkie atrybuty oprócz 'class_type'
# max_info_gain = -1
# selected_attribute = None
# for attribute in attributes:
#     gain = information_gain(data, attribute)
#     if gain > max_info_gain:
#         max_info_gain = gain
#         selected_attribute = attribute
#
# print("Selected attribute with maximum information gain:", selected_attribute)
