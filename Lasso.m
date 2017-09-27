% Set up CVX to obtain the ground truth
cd cvx
    cvx_startup
    cvx_setup
cd ..


%%
N = 100;
d = 10;
A = randn([N, d]);
b = randn(N,1) * 2;
lambda = 0.01;

% cvx Solution
cvx_begin quiet
    variable x(d, 1);
    minimize (0.5 * sum_square(A * x - b) + lambda * norm(x, 1));
cvx_end
x_cvx = x;

% ADMM Solution
tau = 1;
Itr_max = 50;
z = randn(d,1);
y = randn(d,1);
tp1 = inv(A' * A+ 1/tau * eye(d));
tp2 = A' * b;
S   = @(x, a) sign(x) .* max(abs(x)-a, 0);

log = zeros(Itr_max,1);
for i = 1: Itr_max
    % update
    x = tp1 *(tp2 + 1/tau *(z-y));
    z = S(x+y, lambda * tau);
    y = y + 1/tau*(x-z);
    log(i)= log10(norm(x_cvx-x,2));
end

plot(log)
xlabel('Iteration');
ylabel('Difference to the Optimal')
display('Done');





