n = -7:100;
unit_step = [zeros(1, 7), 1, ones(1, 100)];
a = [1; -1.1];
b = 1;
y = filter(b,a, unit_step);
stem(n, y)
