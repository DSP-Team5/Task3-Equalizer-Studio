import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate = 880  # Sample rate (Hz)
duration = 5  # Duration of the audio signal (seconds)
frequency = 440  # Frequency of the sinusoidal waveform (Hz)

# Generate the time array
t = np.linspace(0, duration, int(sample_rate * duration))

# Generate the audio signal (sinusoidal waveform)
audio_signal = np.sin(2 * np.pi * frequency * t)

# Scale the audio signal to the appropriate range (-32768 to 32767 for 16-bit WAV)
scaled_audio_signal = np.int16(audio_signal * 32767)

# Save the audio signal as a WAV file
wavfile.write("test_audio.wav", sample_rate, scaled_audio_signal)

# Plot the waveform
