clear();

Fs_2 = 44100 / 2;
passband = 18000 / Fs_2;
N = 98;
Wn = passband;
type = 'high';

% Päästökaistan maksimivärähtely 0.1 dB
% Estokaistan minimivaimennus 30 dB
% => opintomoniste s.84 taulukko
% => Hanning

window = hanning(N+1)

d = fir1 (N, passband, type, window);

impz(d)
figure
freqz(d)
figure
zplane(d)