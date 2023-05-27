import streamlit as st
import numpy as np
import pandas as pd
import os
from scipy.io import wavfile
from scipy.fft import fftshift, fft, irfft
import functions as fn
import altair as alt
import animation as animation 

st.sidebar.title("Select Mode")
modes = ["Normal", "Music", "Vowels", "Biological Abnormalities"]
mode = st.sidebar.selectbox("Select Mode", modes)
uploaded_file = st.sidebar.file_uploader("Select a signal file", type=["wav", "csv"])

if uploaded_file is not None:
    
    name = uploaded_file.name
    type = uploaded_file.type
    path = os.path.join("temp", uploaded_file.name)
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
        signal_x_axis_before, signal_y_axis_before, sample_rate_before ,sound_info_before = animation.read_audio(name)
        df = pd.DataFrame({'time': signal_x_axis_before[::500], 'amplitude': signal_y_axis_before[:: 500]}, columns=['time', 'amplitude'])
        lines = alt.Chart(df).mark_line().encode( x=alt.X('time', axis=alt.Axis(title='time')),
                                                y=alt.Y('amplitude', axis=alt.Axis(title='amplitude'))).properties(width=500,height=200)
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
            st.altair_chart(lines)

            show_input_spectrogram = st.checkbox("Show Input Spectrogram", value=True)
            if show_input_spectrogram:
                st.subheader("Input Spectrogram")
                # Create spectrogram using Altair or other libraries
                # ...

        with after:
            st.subheader("Output Signal")
            st.altair_chart(lines)

            show_output_spectrogram = st.checkbox("Show Output Spectrogram", value=True)
            if show_output_spectrogram:
                st.subheader("Output Spectrogram")
                # Create spectrogram using Altair or other libraries
                # ...

else:
    fn.welcome_screen()