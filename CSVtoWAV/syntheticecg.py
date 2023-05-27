import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Signal parameters
sampling_rate = 44100  # Adjust as desired
duration = 10  # Duration in seconds

# Generate time axis
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate synthetic ECG signal with noise
ecg_signal = np.sin(2 * np.pi * 1.0 * t) + 0.5 * np.sin(2 * np.pi * 0.2 * t)

# Amplify the signal
amplification_factor = 50
ecg_signal *= amplification_factor

# Normalize signal
ecg_signal /= np.max(np.abs(ecg_signal))

# Convert to int16
ecg_signal_int16 = (ecg_signal * 32767).astype(np.int16)

# Save as .wav file
wavfile.write('synth_ecg_signal.wav', sampling_rate, ecg_signal_int16)

# Plot the ECG signal
plt.figure()
plt.plot(t, ecg_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Synthetic ECG Signal')
plt.show()
