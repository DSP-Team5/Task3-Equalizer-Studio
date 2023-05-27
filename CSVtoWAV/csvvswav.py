import numpy as np
from scipy.io import wavfile
import csv

# Sampling rate
sampling_rate = 44100

# Signal frequency
frequency = 400

# Signal duration (in seconds)
duration = 5

# Generate time array
t = np.arange(0, duration, 1 / sampling_rate)

# Generate signal
signal = np.sin(2 * np.pi * frequency * t)

# Normalize signal
signal /= np.max(np.abs(signal))

# Scale the signal to 16-bit range (-32768 to 32767)
scaled_signal = np.int16(signal * 32767)

# Save as WAV file
wavfile.write('sound_signal.wav', sampling_rate, scaled_signal)

# Save as CSV file
csv_data = np.column_stack((t, signal))
with open('sound_signal.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
