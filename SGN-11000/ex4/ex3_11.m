%a
x = rand(1, 8192);
h=0.05*[ones(1,20),zeros(1,8192-20)];

disp('With fft-> ifft')
tic;
X = fft(x);
H = fft(h);
y1 = ifft(X .* H);
toc;

disp('With conv')
tic;
y2 = conv(h,x);
toc;

plot((1:200),real(y1(1:200)),(1:200),y2(1:200))


results_1 = zeros(size(100));
results_2 = zeros(size(100));
for i=1:100
    x = rand(1, 8192);
    h = 0.05*[ones(1,20),zeros(1,8192-20)];
    temp = zeros(1,100);
    for k=1:100
        tic; 
        ifft(fft(x) .* fft(h));
        temp(k) = toc;
    end
    results_1(i) = sum(temp) / 100;


    for k=1:100
        tic; 
        conv(h,x);
        temp(k) = toc;
    end
    results_2(i) = sum(temp) / 100;
end

plot(1:100, results_1, 'b', 1:100, results_2, 'g')
