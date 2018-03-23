N_range = [16 32 64 128 256 512 1024];

results_1 = zeros(size(N_range));
results_2 = zeros(size(N_range));
for i = 1:size(N_range,2)
    N = N_range(i);
    F=exp(-2*pi*1i*(0:N-1)'*(0:N-1)/N);
    
    temp = zeros(1,100);
    for k=1:100
        tic; 
        F * rand(N,1);
        temp(k) = toc;
    end
    results_1(i) = sum(temp) / 100;
    
    
    for k=1:100
        tic; 
        fft(rand(N,1));
        temp(k) = toc;
    end
    results_2(i) = sum(temp) / 100;
end

plot(N_range, results_1, '-o', N_range, results_2, '-x')
