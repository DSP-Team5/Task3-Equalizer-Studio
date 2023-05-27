
import io
import os
import random
import wave

import altair as alt
import IPython.display as ipd
import librosa
import librosa.display
import numpy as np
import pandas as pd
import pylab
import streamlit as st
from scipy.io.wavfile import write
from scipy.signal import find_peaks


class variabls :
    points_num =1000
    count=0








# Plot a Chart
def plot_animation(df):
    brush = alt.selection_interval()
    lines = alt.Chart(df).mark_line().encode(
        x=alt.X('time', axis=alt.Axis(title='time')),
        y=alt.Y('amplitude', axis=alt.Axis(title='amplitude')),
    ).properties(
        width=500,
        height=200
    ).add_selection(
        brush).interactive()
    return lines




