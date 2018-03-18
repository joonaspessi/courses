load gong
soundsc(y, Fs)

disp('normaali');
pause;

v = [-0.2427 -0.2001 0.7794 -0.2001 -0.2427];
z = conv(v, y);

disp('suodatettu');
soundsc(z, Fs)

pause;

disp('clap');


load seiska.mat
[h,Fs] = audioread('hall.wav');

soundsc(x, Fs)
disp('conv');

pause;
zz = conv(h, y);

soundsc(zz, Fs)