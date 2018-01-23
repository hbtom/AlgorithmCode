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
tic
cvx_begin quiet
    variable x(d, 1);
    minimize (0.5 * sum_square(A * x - b) + lambda * norm(x, 1));
    subject to
        x >= 0;
cvx_end
x_cvx = x;
time_cvx = toc;

% ADMM Solution
tau = .9;
Itr_max = 2000;
z = randn(d,1);
y = randn(d,1);
tp1 = inv(A' * A+ 1/tau * eye(d));
tp2 = A' * b;
S   = @(x, y,lambda,rho) max(x + y - lambda*tau, 0);

log = zeros(Itr_max,1);
tic;
for i = 1: Itr_max
    % update
    x = tp1 *(tp2 + 1/tau *(z-y));
    z = S(x, y, lambda, tau);
    y = y + 1/tau*(x-z);
    log(i)= log10(norm(x_cvx-x,2));
end
time_admm = toc;

plot(log)
xlabel('Iteration');
ylabel('Difference to the Optimal')
display('Done');





