import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.io import wavfile
from scipy.fft import fftshift, fft, irfft
import functions as fn

# normalIndex=[] 
# numofPoints=0
# magnitude_n=[]
# magnitude=[]
# freq=[] 
# numpoints = []
# startIndex =[]
# samplfreq=0
# lines1=any
# optional =  False
# # -------------------------------------------------------------------------------------------------------------#
st.sidebar.title("Select Mode")
modes = ["Normal", "Music", "Vowels", "Biological Abnormalities"]
mode = st.sidebar.selectbox("Select Mode", modes)
uploaded_file = st.sidebar.file_uploader("Select a signal file", type=["wav", "csv"])

if uploaded_file is not None:
    
    name = uploaded_file.name
    type = uploaded_file.type
    if fn.validate_file_type(name, ["wav"]):
        # Load wav file
        signal = fn.load_signal(uploaded_file)
    elif fn.validate_file_type(name, ["csv"]):
        # Load csv file
        # ...
        # Conversion logic
        # ...
        signal = np.zeros(44100)  # Placeholder signal
        wavfile.write("temp.wav", 44100, signal)
        signal = fn.load_signal("temp.wav")
        os.remove("temp.wav")  # Remove temporary wav file
    else:
        st.error("Invalid file type. Only WAV and CSV files are supported.")
else:
    fn.welcome_screen()

if mode:
    if type == "audio/wav":
        modified_signal = fn.mode_conditions(mode, signal)
        if mode == "Normal":
            st.title("Normal mode")
            before, after = st.columns(2)
            # Customize sliders for Normal mode
            label = ["Slider 1", "Slider 2", "Slider 3", "Slider 4", "Slider 5", "Slider 6", "Slider 7", "Slider 8", "Slider 9", "Slider 10"]
            frequencies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
            sliders_values = fn.creating_new_slider(label)
            # Apply equalizer to generate output signal
            output_signal = fn.apply_equalizer(modified_signal, sliders_values)
        elif mode == "Music":
            # Implement Music mode
            st.title("Music Studio")
            before, after = st.columns(2)
        elif mode == "Vowels":
            # Implement Vowels mode
            st.title("Vowel Separation Studio")
            before, after = st.columns(2)
        elif mode == "Biological Abnormalities":
            # Implement Biological Abnormalities mode
            st.title("Biological Abnormalities Studio")
            before, after = st.columns(2)

        with before:
            st.subheader("Input Signal")
            fig1, ax1 = plt.subplots(figsize=((5, 1.5)))
            ax1.plot(signal)
            ax1.set_title("Input Signal")
            ax1.set_xlabel("Time")
            ax1.set_ylabel("Amplitude")
            st.pyplot(fig1)

            show_input_spectrogram = st.checkbox("Show Input Spectrogram", value=True)
            if show_input_spectrogram:
                st.subheader("Input Spectrogram")
                fig3, ax3 = plt.subplots(figsize=((5, 1.5)))
                input_spectrogram, _, _, _ = ax3.specgram(signal, Fs=44100, vmin=-100, vmax=100)
                ax3.set_title("Input Spectrogram")
                st.pyplot(fig3)
                

        with after:
            st.subheader("Output Signal")
            fig2, ax2 = plt.subplots(figsize=((5, 1.5)))
            ax2.plot(modified_signal)
            ax2.set_title("Output Signal")
            ax2.set_xlabel("Time")
            ax2.set_ylabel("Amplitude")
            st.pyplot(fig2)

            show_output_spectrogram = st.checkbox("Show Output Spectrogram", value=True)
            if show_output_spectrogram:
                st.subheader("Output Spectrogram")
                fig4, ax4 = plt.subplots(figsize=((5, 1.5)))
                output_spectrogram, _, _, _ = ax4.specgram(modified_signal, Fs=44100, vmin=-100, vmax=100)
                ax4.set_title("Output Spectrogram")
                st.pyplot(fig4)


