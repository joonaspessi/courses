n = 0:100;

x = sin(0.05 * 2*pi*n);

b = [0.0349 0.4302 -0.5698 0.4302  0.0349];
a = 1;
y_filter = filter(b, a, x);

y_real = 0.3050 * sin(0.05 * 2 * pi * n - 0.6283);

plot(n, x, n, y_filter, n, y_real)
