clear()

load("numero"); % imports salainen

N = 98;
F = [0, 0.33, 0.36, 1];
A = [0, 0, 1, 1];

f = firpm(N, F, A);

freqz(f);

y_filter = filter(f, 1, salainen);

sound(y_filter);