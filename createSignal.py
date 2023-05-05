import numpy as np
from scipy.io import wavfile
import animation

# Define the sampling frequency and duration
fs = 44100 # Sampling frequency (Hz)
dur = 5 # Duration (s)

# Define the frequency of the sine wave
f = 500 # Frequency (Hz)

# Generate the sine wave
t = np.arange(0, dur, 1/fs) # Time vector
y = np.sin(2*np.pi*f*t) # Sine

# Apply a low-pass filter using the method
fc = 1000 # Cutoff frequency (Hz)
order = 4 # Order of the filter
h = np.sin(2*np.pi*fc*t)/(np.pi*t + np.finfo(float).eps) # Ideal low-pass filter impulse response
w = np.hamming(len(h)) # Window function
h_windowed = h*w # Windowed impulse response
h_windowed = h_windowed/np.sum(h_windowed) # Normalize the filter coefficients
b = h_windowed # Numerator coefficients
a = 1 # Denominator coefficients
y_filtered = np.convolve(b, y, mode='same') # Filtered signal

# Save the waveform as a WAV file with float32 sample width
filename = 'sine_wave.wav'
wavfile.write(filename, fs, y_filtered.astype(np.float32))


# Read the waveform from the WAV file using animation.read_audio

