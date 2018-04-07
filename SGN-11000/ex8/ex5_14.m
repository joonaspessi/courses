% Ylipäästösuodin
% Päästökaista [1240 Hz, 4096 Hz]
% Estokaista [0 kHz, 820 Hz]
% Päästökaistan maksimivärähtely 0.1 dB
% Estokaistan minimivaimennus 60 dB
% Näytteenottotaajuus 8192 Hz

% Käytetään Blackman ikkunaa vaatimusten toteuttamiseksi
% kts. opintomoniste s.84

clear();
type = 'high';
Fs = 8192;

passband_limit = 2 * 1240 / Fs;
stopband_limit = 2 * 820 / Fs;

N_candidate = 5.5 / ((1240-820) / Fs);
% Pyöristetään ylöspäin seuraavaan parittomaan
N = 2*ceil(N_candidate/2)+1;

window = blackman(N);

d = fir1 (N - 1, passband_limit, type, window);

figure('Name', 'freq')
freqz(d)
