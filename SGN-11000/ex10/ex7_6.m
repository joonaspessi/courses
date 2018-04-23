Wp = 0.15 * 2;
Ws = 0.1 * 2;
Rp = 0.1;
Rs = 50;

[N,Wn] = ellipord(Wp, Ws, Rp, Rs);
[b,a] = ellip(N, Rp, Rs, Wn, 'high');

aq11 = quant(a, 1/2^11);
bq11 = quant(b, 1/2^11);

fvtool(b,a, bq11, aq11)