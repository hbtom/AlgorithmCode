%% A size m x n matrix with rank r has observation ratio 0.9
m = 20;
n = 20;
r = 2;
p = 0.7;

% geerate missing matrix M_miss and obsevation indicator matrix P_Omega
M = randn(m,r) * randn(r, n);
Miss= randsample(m *n, round((1-p)*m*n));
M_miss=M; M_miss(Miss)=0;
P_Omega = ones(m,n);
P_Omega(Miss)= 0;
% ****************************************************** %
% SVT algorithm
% min || X ||_*     s.t.    P_Omega.*(X) = P_Omega.*(M)  %
% ****************************************************** %
Y = zeros(size(M_miss));    % initialization
maxIter = 10000;
tau = 5*sqrt(m*n);          % parameter tau, important
delta = 1.2/p;              % updating rate, important
for i=1:maxIter
    [U S V] = svd(Y);
    S = S-tau;S(S<0)=0;
    X = U * S * V';
    Y = Y + delta * (M_miss -X).*P_Omega;
end
disp(norm(X-M, 'fro')/norm(M, 'fro'));
disp(norm(P_Omega.*(X-M), 'fro')/norm(P_Omega.*M, 'fro'));