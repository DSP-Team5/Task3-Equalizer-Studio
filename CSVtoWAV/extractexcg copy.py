import wfdb
import numpy as np
from scipy.io import wavfile

# Load ECG record
record_name = '103'  # Replace with the actual record name (without file extension)
record = wfdb.rdrecord(record_name)

# Extract ECG signal
ecg_signal = record.p_signal.flatten()

# Normalize signal
ecg_signal /= np.max(np.abs(ecg_signal))

# Scale the signal to 16-bit range (-32768 to 32767)
scaled_signal = np.int16(ecg_signal * 32767)

np.savetxt('ecg_signal.csv', ecg_signal, delimiter=',')
# Save as WAV file
wavfile.write('ecg_signal.wav', record.fs, scaled_signal)
