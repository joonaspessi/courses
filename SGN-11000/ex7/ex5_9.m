clear();

Fs = 44100;
Fs_2 = Fs / 2;
passband = 18000 / Fs_2;
Wn = passband;
type = 'high';

% Päästökaistan maksimivärähtely 0.1 dB
% Estokaistan minimivaimennus 30 dB
% => opintomoniste s.84 taulukko
% => Hanning 
N_candidate = 3.1 / (3000 / Fs);

% Pyöristetään ylöspäin seuraavaan parittomaan
N = 2*ceil(N_candidate/2)+1;
window = hanning(N);
d = fir1(N - 1, passband, type, window);

figure('Name', 'impz')
impz(d)

figure('Name', 'freq')
freqz(d)

figure('Name', 'zplane')
zplane(d)
