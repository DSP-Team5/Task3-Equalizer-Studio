import pandas as pd
import plotly.graph_objects as go

# Read data from the CSV file
df = pd.read_csv('ecg_signal.csv', header=None, names=['Amplitude'])

# Create the animated plot
fig = go.Figure(
    data=go.Scatter(x=df.index, y=df['Amplitude'], mode='lines'),
    layout=go.Layout(
        title='ECG Signal',
        xaxis=dict(title='Time'),
        yaxis=dict(title='Amplitude'),
    ),
    frames=[go.Frame(data=[go.Scatter(x=df.index[:i+1], y=df['Amplitude'][:i+1], mode='lines')]) for i in range(len(df))]
)

# Set animation duration and mode
fig.update_layout(updatemenus=[dict(type='buttons', buttons=[dict(label='Play', method='animate', args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}])])])

# Display the animated plot
fig.show()
