clear;
load gong.mat;

[gong3,  t] = kvant(y, 3)
[gong7,  t] = kvant(y, 7)
[gong11, t] = kvant(y, 11)
[gong15, t] = kvant(y, 15)

y = audioread('seiska.wav');

[seiska3,  t]  = kvant(y, 3)
[seiska7,  t]  = kvant(y, 7)
[seiska11, t]  = kvant(y, 11)
[seiska15, t]  = kvant(y, 15)

function [k, t] = kvant(y, x)
    z = quant(y, 1/2^x);
    figure()
    stem(y-z);
    axis(tight);
    k = var(y-z);
    t = 2^(-2*x)/12;
end
