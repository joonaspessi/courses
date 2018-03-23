load corrupt.mat
load handel

y=y(1:2^16);
z=z(1: 2^16);

H = fft(z) ./ fft(y);

h = ifft(H);

plot((1:10),h(1:10))