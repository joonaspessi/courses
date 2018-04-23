N = 10000; % Test signal length
x = [1; 1; zeros(N,1)]; % Input
y = zeros(size(x)); % Output

% Kirjoita alle y(n):ään suodatuksen tulos kvantisoinnin
% jälkeen, kun suodin on H(z) = 1 / (1 + 0.5z^(-1)).

for n = 2:N
    y(n) = x(n) - 0.5*y(n-1);
    y(n) = quant(y(n), 1/2^5);
end
    
stem(y(1:100), 'filled')

soundsc(y,8000)