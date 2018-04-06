clear()
t=0:1/8192:4;
y=chirp(t,0,1,1000);

disp("original spectogram")
spectrogram(y);




b = [0.0675; 0.1349; 0.0675];
a = [1; -1.143; 0.4128];

pause();
disp("Filter details")
freqz(b, a)

y_filter = filter(b, a, y);

pause();
disp("signal after filter")
spectrogram(y_filter);

