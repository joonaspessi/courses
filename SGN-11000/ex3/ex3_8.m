f = 1000;
Fs = 8192;
n = (1:1:Fs);
x = sin((2 * pi * n * f) / Fs);
X = fft(x);

plot(n, abs(X))