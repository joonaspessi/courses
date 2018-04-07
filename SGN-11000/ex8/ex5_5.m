clear();
N = 41;
n = -(N-1)/2:(N-1)/2;
fc = 0.3;
h = 2 * fc * sinc(n * 2 * fc);

figure('Name', 'a')
%a
subplot(211);
stem(n, h);
title('Impulssivaste');

subplot(212);
[H, W] = freqz(h);
plot(W / (2 * pi), 20 * log10(abs(H)));
title('amplitudivaste: Ensimmäinen värähtely -21db');

%b
N = 61;
n = -(N-1)/2:(N-1)/2;
fc = 0.3;
h = 2 * fc * sinc(n * 2 * fc);

figure('Name', 'b')
subplot(211);
stem(n, h);
title('Impulssivaste')

subplot(212);
[H, W] = freqz(h);
plot(W / (2 * pi), 20 * log10(abs(H)));
title('amplitudivaste, Ensimmäien värähtely ~-21db');
% N kasvatus ei pienennä estokaistan minimivärähtelyä

%b
N = 301;
n = -(N-1)/2:(N-1)/2;
fc = 0.3;
h = 2 * fc * sinc(n * 2 * fc);

figure('Name', 'c')
subplot(211);
stem(n, h);
title('Impulssivaste')

subplot(212);
[H, W] = freqz(h);
plot(W / (2 * pi), 20 * log10(abs(H)));
title('amplitudivaste, Ensimmäien värähtely ~-21db');
% N kasvattamisella ei voida vaikuttaa estokaistan vaimennukseen

