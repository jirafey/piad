from typing import Tuple, Any

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.image as mpimg
from numpy import ndarray, dtype


def generate_discretized_sine_wave(f: int, Fs: int) -> tuple[ndarray[Any, dtype[Any]], Any]:
    dt = 1 / Fs
    t = np.arange(0, 1, dt)
    s = np.sin(2 * np.pi * f * t)
    return t, s

# Częstotliwość sygnału sinusoidalnego
frequency = 10

# Częstotliwości próbkowania
sampling_frequencies = [20, 21, 30, 45, 50, 100, 150, 200, 250, 1000]

for Fs in sampling_frequencies:
    t, s = generate_discretized_sine_wave(frequency, Fs)
    plt.figure()
    plt.plot(t, s)
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.title(f'Zdyskretyzowany sygnał sinusoidalny (f = {frequency} Hz, Fs = {Fs} Hz)')
    plt.show()
#  twierdzenie Nyquista-Shannona.

# aliasing.


# Open and display the image
img:ndarray = mpimg.imread('robal.png')
img2: ndarray = mpimg.imread('robal.png')
img3: ndarray = mpimg.imread('robal.png')
img4: ndarray = mpimg.imread('robal.png')
# plt.imshow(img)
# plt.axis('off')  # Turn off axis numbers and ticks
# plt.show()


# KWANTYZACJA

print(img.ndim)

shape = img.shape

print(shape[2])

def grayscale():
    i: int
    j: int
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            a = img2[i][j]
            b = img3[i][j]
            c = img3[i][j]
            img2[i][j] = (max(a[0], a[1], a[2]) + min(a[0], a[1], a[2])) / 2
            img3[i][j] = (b[0] + b[1] + b[2]) / 3
            img4[i][j] = (c[0] * 0.21) + (c[1] * 0.72) + (c[2] * 0.07)

    for i in [img2, img3, img4]:
        plt.imshow(i)
        plt.axis('off')  # Turn off axis numbers and ticks
        plt.show()

# grayscale()

