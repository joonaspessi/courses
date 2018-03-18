f = 1000;
Fs = 8192;
n = (1:1:Fs);
x = sin((2 * pi * n * f) / Fs);
soundsc(x)

disp('continue?');
pause;


f = 2000;
x = sin((2 * pi * n * f) / Fs);
soundsc(x)

disp('continue?');
pause;

f = 3000;
x = sin((2 * pi *n * f) / Fs);
soundsc(x)

disp('continue?');
pause;

f = 6000;
x = sin((2 * pi *n * f) / Fs);
soundsc(x)

disp('continue?');
pause;

f = 7000;
x = sin((2 * pi *n * f) / Fs);
soundsc(x)

disp('continue?');
pause;

f = 8000;
x = sin((2 * pi *n * f) / Fs);
soundsc(x)