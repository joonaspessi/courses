% a

delta=[1,zeros(1,127)];
a = [1 0.9];
b = 1;
y = filter(b, a, delta);
disp('a');
stem(y)
pause();

y = impz(b, a, 127);
disp('a impz');
stem(y)
pause();

%b
a = [1 -0.6 0.3];
b = [0.2 -0.5 0.8];
y2 = filter(b, a, delta);
disp('b');
stem(y2);
pause();

disp('b impz');
impz(b, a, 127);
pause();

%c
a = [1 -0.5 -0.6];
b = [1 0.5 0.25];
y2 = filter(b, a, delta);
disp('c');
stem(y2);
pause();

disp('c impz');
impz(b,a, 127);

% =>> c ei ole stabiili