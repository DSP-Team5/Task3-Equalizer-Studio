import csv
import numpy as np
import wave
import os
from tkinter import filedialog

def read_csv(csv_file):
  """Reads a CSV file and returns a NumPy array.

  Args:
    csv_file: The path to the CSV file.

  Returns:
    A NumPy array containing the data from the CSV file.
  """

  with open(csv_file, "r") as f:
    reader = csv.reader(f)
    header = next(reader)

    # Get the data from the CSV file.
    data = []
    for row in reader:
      data.append([float(value) for value in row])

    return np.array(data)

def write_wav(data, wav_file):
  """Writes a NumPy array to a WAV file.

  Args:
    data: The NumPy array containing the data to write.
    wav_file: The path to the WAV file to write to.
  """

  # Create a wave file object.
  wf = wave.open(wav_file, "wb")

  # Set the wave file parameters.
  wf.setnchannels(1)
  wf.setsampwidth(2)
  wf.setframerate(1000)

  # Write the data to the wave file.
  wf.writeframes(data.tobytes())

  # Close the wave file.
  wf.close()

def main():
  # Get the path to the CSV file.
  csv_file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

  # Read the data from the CSV file.
  data = read_csv(csv_file)

  # Get the path to the WAV file.
  wav_file = os.path.splitext(csv_file)[0] + ".wav"

  # Write the data to the WAV file.
  write_wav(data, wav_file)

if __name__ == "__main__":
  main()
