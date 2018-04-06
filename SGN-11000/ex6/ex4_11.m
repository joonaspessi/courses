clear();
b = [0.0122 0.0226 0.0298 0.0204 0.0099];
a = [1 -0.9170 0.054 -0.2410 0.1990];


zplane(b, a)
disp("click to continue")
figure
freqz(b, a)
figure
impz(b, a)
pause()

disp("Inverted system")

figure
zplane(a, b)
disp("click to continue")
figure
freqz(a, b)
figure
impz(a, b)