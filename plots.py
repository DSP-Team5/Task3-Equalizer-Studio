import time
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.fft import fftshift, fft, irfft
import functions as fn
import altair as alt
import animation as animation

normalIndex=[] 
numofPoints=0
magnitude_n=[]
magnitude=[]
freq=[] 
numpoints = []
startIndex =[]
samplfreq=0
output_lines=any
optional =  False
# -------------------------------------------------------------------------------------------------------------#
if "size" not in st.session_state:
    st.session_state['size'] = 0
if "counter" not in st.session_state:
    st.session_state['counter'] = 0
if "btn_state" not in st.session_state:
    st.session_state['btn_state'] = 0
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
        signal_x_axis_before, signal_y_axis_before, sample_rate_before ,sound_info_before = fn.read_audio(name)
        
        df = pd.DataFrame({'time': signal_x_axis_before[::500], 'amplitude': signal_y_axis_before[:: 500]}, columns=['time', 'amplitude'])
        input_lines = alt.Chart(df).mark_line().encode( x=alt.X('time', axis=alt.Axis(title='time')),y=alt.Y('amplitude', axis=alt.Axis(title='amplitude'))).properties(width=300,height=190)
        
        samplfreq, audio = wavfile.read(name)  
        magnitude , freq=fn.fourierTansformWave(audio ,samplfreq)  
        points_per_freq = np.ceil(len(freq) / (samplfreq / 2) )  # number of points per  frequancy 
        points_per_freq = int(points_per_freq)
        modified_signal = fn.mode_conditions(mode, signal)
        
        if mode == "Normal":
            st.title("Normal mode")
            before, after = st.columns(2)
            max_freq = np.max(freq)  # get the maximum frequency of the audio file
            num_bins = 10  # replace with the number of bins you want to create
            bin_width = max_freq / num_bins
            label = []
            for i in range(num_bins):
                start_freq = i * bin_width
                end_freq = (i + 1) * bin_width 
                label.append("{}  Hz".format(int(end_freq)))
            # read file          
            sliders = fn.creating_new_slider(label)
            normalIndex, numofPoints = fn.bandLength(freq)  # get index of slider in how point will change when move slider 
            numpoints = []
            startIndex = []
            for i in range(num_bins):
                if i < num_bins - 1:
                    numpoints.append(int(numofPoints / 2))
                else:
                    numofPoints = (numofPoints / 2) * (num_bins - 1) + numofPoints
                    numpoints.append(int(numofPoints))
                startIndex.append(int(i * bin_width / max_freq * len(freq)))
        elif mode == "Music":
            # Implement Music mode
            st.title("Music Studio")
            before, after = st.columns(2)
            label= [" Drums","piano" ,"guitar"]
            sliders =fn.creating_new_slider(label)
            frequencies = [0, 500,  2000, 7000]
            for i in range(len(label)):
                    numpoints.insert(i,np.abs(frequencies[i] * points_per_freq - frequencies[i+1] * points_per_freq))
                    startIndex.insert(i,frequencies[i] * points_per_freq)
        elif mode == "Vowels":
            # Implement Vowels mode
            st.title("Vowel Separation Studio")
            before, after = st.columns(2)
            label= ["SH","O", 'D', 'R']
            sliders =fn.creating_new_slider(label)
            frequencies = [[[900, 9300]], [[10, 2300]], [[100, 600], [2000, 4000]], [[1200, 5000]]]
            
        elif mode == "Biological Abnormalities":
            # Implement Biological Abnormalities mode
            st.title("Biological Abnormalities Studio")
            before, after = st.columns(2)
            
        magnitude_spactro=magnitude
        spectrogramOrigin = irfft(magnitude_spactro)
        # plot spactro (before)
        beforeSpectro = plt.figure(figsize=(4, 1.5))
        plt.specgram(spectrogramOrigin, Fs=samplfreq, vmin=-50, vmax=50 )
        plt.colorbar()
        if(mode == "Vowels"):
            magnitude = fn.Vowels(points_per_freq, sliders, frequencies, magnitude)
        else:
            magnitude=fn.modify_wave(magnitude , numpoints , startIndex , sliders, len(label))
            
        new_sig = irfft(magnitude)
        norm_new_sig = np.int16(new_sig * (32767 / new_sig.max()))
        write("output.wav", samplfreq, norm_new_sig)
        signal_x_axis_after, signal_y_axis_after, sample_rate_after ,sound_info_after = fn.read_audio("output.wav")    # Read Audio File
        df1 = pd.DataFrame({'time': signal_x_axis_after[::500], 'amplitude': signal_y_axis_after[:: 500]}, columns=['time', 'amplitude'])
        output_lines = alt.Chart(df1).mark_line().encode( x=alt.X('time', axis=alt.Axis(title='time')),
                                                y=alt.Y('amplitude', axis=alt.Axis(title='amplitude'))).properties(width=300,height=190)
        with before:
            st.subheader("Before")
            st.audio(signal, format='audio/wav', sample_rate=44100)
            #st.subheader("Input Signal")
            line_plot_before=st.altair_chart(input_lines)

            show_input_spectrogram = st.checkbox("Show Input Spectrogram", value=True)
            if show_input_spectrogram:
                #st.subheader("Input Spectrogram")

                st.pyplot(beforeSpectro)

            # Audio player for "before" signal


        with after:
            st.subheader("After")
            st.audio(norm_new_sig, format='audio/wav', sample_rate=44100)
            #st.subheader("Output Signal")
            line_plot_after=st.altair_chart(output_lines)
            show_output_spectrogram = st.checkbox("Show Output Spectrogram", value=True)
            if show_output_spectrogram:
                #st.subheader("Output Spectrogram")
                afterspectro = plt.figure(figsize=(4, 1.5))
                plt.specgram(new_sig, Fs=samplfreq, vmin=-50, vmax=50)
                plt.colorbar()
                st.pyplot(afterspectro)
            # Audio player for "after" signal
            start_btn_col,reset_btn_col =st.sidebar.columns(2)
            with start_btn_col:
                placeholder=st.empty()
                start_btn =  placeholder.button('Start')
            with reset_btn_col:
                reset_btn =st.button('Reset')
            N = df.shape[0]  # number of elements in the dataframe
            burst = int(len(df1)/4)       # number of elements (months) to add to the plot
            size = burst     # size of the current dataset 
            if start_btn  and st.session_state["btn_state"]==0:
                st.session_state['btn_state']=1
                placeholder.empty()
                start_btn=placeholder.button('Pause')
                for i in range(st.session_state["size"]+burst, N - burst):
                    i=st.session_state['counter']
                    step_df  = df.iloc[i:st.session_state['size']]
                    step_df1 = df1.iloc[i:st.session_state['size']]

                    input_lines  = animation.plot_animation(step_df)
                    output_lines = animation.plot_animation(step_df1)


                    line_plot_befor  = line_plot_before.altair_chart(input_lines)
                    line_plot_after= line_plot_after.altair_chart(output_lines)

                    st.session_state['size'] = i + burst
                    if st.session_state['size'] >= N:
                        st.session_state['size'] = N - 1
                    time.sleep(.00000000001)
                    st.session_state['counter'] += 1
            
            if  st.session_state["btn_state"]==1:
                st.session_state["btn_state"]=0
                step_df  = df.iloc[st.session_state['counter']:st.session_state['size']]
                step_df1 = df1.iloc[st.session_state['counter']:st.session_state['size']]
                input_lines  = animation.plot_animation(step_df)
                output_lines = animation.plot_animation(step_df1)
                line_plot_befor  = line_plot_before.altair_chart(input_lines)
                line_plot_after= line_plot_after.altair_chart(output_lines) 
            if reset_btn_col:
                st.session_state['size'] =0
                st.session_state['counter'] = 0
                st.session_state["btn_state"]=0


else:
    fn.welcome_screen()
