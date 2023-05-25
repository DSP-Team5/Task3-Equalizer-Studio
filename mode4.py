import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

def generate_signal(duration, sampling_rate):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sin(2 * np.pi * 1.0 * t) + np.sin(2 * np.pi * 4.0 * t)
    return t, signal

def apply_ecg_arrhythmia(signal, magnitude):
    modified_signal = signal + magnitude * np.random.normal(0, 0.1, len(signal))
    return modified_signal

st.sidebar.title("Biological Signal Abnormalities")
mode = st.sidebar.selectbox("Select Mode", ["Mode 1", "Mode 2", "Mode 3", "Mode 4"])

st.title("Biological Signal Abnormalities")

if mode == "Mode 4":
    st.subheader("ECG Arrhythmia")
    magnitude = st.slider("Magnitude", 0.0, 1.0, 0.5, 0.1)

    show_spectrograms = st.checkbox("Show Spectrograms")

    duration = 10.0  # Duration of the signal in seconds
    sampling_rate = 1000  # Number of samples per second
    t, signal = generate_signal(duration, sampling_rate)
    modified_signal = apply_ecg_arrhythmia(signal, magnitude)

    fig = plt.figure(figsize=(12, 6))
    gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])

    ax1.plot(t, signal)
    ax1.set_title("Input Signal")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Amplitude")

    ax2.plot(t, modified_signal)
    ax2.set_title("Output Signal")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Amplitude")

    st.pyplot(fig)

    if show_spectrograms:
        input_spectrogram = np.abs(np.fft.fftshift(np.fft.fft(signal))) ** 2
        output_spectrogram = np.abs(np.fft.fftshift(np.fft.fft(modified_signal))) ** 2

        fig, axs = plt.subplots(2, 1, figsize=(12, 6))
        sns.heatmap(input_spectrogram.reshape(1, -1), cmap="hot", ax=axs[0])
        axs[0].set_title("Input Spectrogram")

        sns.heatmap(output_spectrogram.reshape(1, -1), cmap="hot", ax=axs[1])
        axs[1].set_title("Output Spectrogram")

        st.pyplot(fig)
