import numpy as np
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

def generate_discretized_sine_wave(f, Fs):
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
img = mpimg.imread('robal.png')
plt.imshow(img)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()
