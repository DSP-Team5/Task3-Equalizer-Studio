import csv
import numpy as np
from scipy.io import wavfile

# Read CSV file
def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

# Extract ECG signal from CSV data
def extract_ecg_signal(data):
    ecg_signal = []
    for row in data:
        ecg_signal.append(float(row[0]))  # Assuming the ECG signal is in the first column
    return np.array(ecg_signal)

# Convert ECG signal to WAV file
def convert_to_wav(ecg_signal, sample_rate, output_file):
    wavfile.write(output_file, sample_rate, ecg_signal)

# Main function
def csv_to_wav(csv_file, sample_rate, wav_file):
    # Read CSV file
    csv_data = read_csv(csv_file)

    # Extract ECG signal
    ecg_signal = extract_ecg_signal(csv_data)

    # Convert to WAV file
    convert_to_wav(ecg_signal, sample_rate, wav_file)

# Specify the CSV file path, sample rate, and output WAV file path
csv_file = 'ecg-data.csv'
sample_rate = 44100  # Specify the appropriate sample rate
wav_file = 'file.wav'

# Convert CSV to WAV
csv_to_wav(csv_file, sample_rate, wav_file)
