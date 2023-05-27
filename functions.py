import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy
from scipy.io import wavfile
import streamlit.components.v1 as components
from tkinter import HIDDEN
import pandas as pd
import functions as fn
from scipy.io.wavfile import write
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq, irfft, fft, fftshift
import numpy as np
import numpy.fft as fft
import librosa.display
import matplotlib.pyplot as plt
import plotly_express as px
import IPython.display as ipd
import librosa
import altair as alt
import wave
import io
import pylab
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "build")
_vertical_slider = components.declare_component("vertical_slider", path=build_dir)

def fourierTansformWave(audio=[], sampfreq=44100):
    try:
        audio = audio[:, 0]
    except:
        audio = audio[:]

    #  Fourier transform
    fourier_transform_magnitude = rfft(audio)
    fourier_transform_freq = rfftfreq(len(audio), 1 / sampfreq)

    return fourier_transform_magnitude, fourier_transform_freq
def modify_wave(
    magnitude=[], numPoints=0, startIndex=0, scalerNumber=[], sliders_num=0
):
    for i in range(sliders_num):
        magnitude[startIndex[i] : numPoints[i] + startIndex[i]] *= scalerNumber[i]
    return magnitude


# --------------------------------------------- bands -------------------------------------------
def bandLength(freq=[]):
    length_band = len(freq) / 10
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = int(i * length_band)

    return arr, len(freq) / 10  #
def Vowels(points_per_freq, sliders, frequencies, fourier_frequency):
    vowel = ["sh", "M", "D", "R"]
    for i in range(len(frequencies)):
        # print(frequencies[i][i])
        for j in range(len(frequencies[i])):
            # print(vowel[i],frequencies[i][j][0])
            # print(vowel[i],frequencies[i][j][1])
            signal = fourier_frequency[
                int(points_per_freq * frequencies[i][j][0]) : int(
                    points_per_freq * frequencies[i][j][1]
                )
            ]
            triangle_window = scipy.signal.windows.triang(len(signal))

            if sliders[i] < 1:
                value = 10 ** (-100000 * triangle_window)
            else:
                value = 10 ** (((sliders[i] - 1) / 10) * triangle_window)
            fourier_frequency[
                int(points_per_freq * frequencies[i][j][0]) : int(
                    points_per_freq * frequencies[i][j][1]
                )
            ] *= value
    return fourier_frequency

def vertical_slider(value, step, min=min, max=max, key=None):
    slider_value = _vertical_slider(
        value=value, step=step, min=min, max=max, key=key, default=value
    )
    return slider_value

def creating_new_slider(label):
    columns = st.columns(len(label))
    sliders_values = []
    for index in range(len(label)):
        with columns[index]:
            slider = vertical_slider(1, step=1, min=0, max=5, key=index)
            sliders_values.append(slider)
            st.write(label[index])
    return sliders_values

def load_signal(file_path):
    sampling_rate, signal = wavfile.read(file_path)
    return signal

def read_audio(audio_file):
    obj = wave.open(audio_file, 'r')
    sample_rate   = obj.getframerate()                           # number of samples per second
    n_samples     = obj.getnframes()                             # total number of samples in the whole audio
    signal_wave   = obj.readframes(-1)                           # amplitude of the sound
    duration      = n_samples / sample_rate                      # duration of the audio file
    sound_info    = pylab.fromstring(signal_wave, 'int16')
    signal_y_axis = np.frombuffer(signal_wave, dtype=np.int16)
    signal_x_axis = np.linspace(0, duration, len(signal_y_axis))
    return signal_x_axis, signal_y_axis, sample_rate,  sound_info

def validate_file_type(file_name, allowed_types):
    ext = os.path.splitext(file_name)[1][1:].lower()
    return ext in allowed_types
def apply_equalizer(signal, slider_values):
    modified_signal = signal.copy()
    # Implement the logic to modify the signal based on the slider values
    # You can use libraries like scipy or create your own algorithm
    return modified_signal
def mode_conditions(mode, signal):
    modified_signal = signal.copy()
    if mode == "Normal":
        # Implement Normal mode conditions
        pass
    elif mode == "Music":
        # Implement Music mode conditions
        pass
    elif mode == "Vowels":
        # Implement Vowels mode conditions
        pass
    elif mode == "Biological Abnormalities":
        # Implement Biological Abnormalities mode conditions
        pass
    return modified_signal

def welcome_screen():
    st.markdown(
        """
        <style>
        .title {
            color: #FF5733;
            font-size: 30px;
            margin-bottom: 20px;
        }
        .team-members {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .member {
            margin-left: 20px;
        }
        .choose-file {
            font-size: 20px;
            margin-top: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<p class='title'>Welcome to Signal Equalizer Studio</p>", unsafe_allow_html=True)
    st.markdown("<p class='team-members'>Team Members:</p>", unsafe_allow_html=True)
    st.markdown("<p class='member'>- Ahmed Tarek</p>", unsafe_allow_html=True)
    st.markdown("<p class='member'>- Ammar Yasser</p>", unsafe_allow_html=True)
    st.markdown("<p class='member'>- Hanan Tawfik</p>", unsafe_allow_html=True)
    st.markdown("<p class='member'>- Mohamed Hamed</p>", unsafe_allow_html=True)
    st.markdown("<p class='choose-file'>Choose a file to get started</p>", unsafe_allow_html=True)
