ecg = load('1.csv')
plot(ecg)
audiowrite('ecg.wav', ecg, 44100)
