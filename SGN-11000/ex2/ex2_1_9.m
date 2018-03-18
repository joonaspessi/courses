load("seiska.mat");


F = 16384;
soundsc(x, F)

disp('Normaali');
pause;

y=x(1:2:length(x));
soundsc(y, F/2);

disp('Laskostunut');
pause;

y = decimate(x,2);
soundsc(y, F/2);

disp('Decimated');
pause;