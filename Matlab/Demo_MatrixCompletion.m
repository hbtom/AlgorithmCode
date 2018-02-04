clear all; clc; close all;
m = 1000;
n = 1000;
r = 20;
p = 0.5;

% generate matrix
Data        = randn(m, r) * randn(r, n);
Omega       = zeros(m, n);Omega(randsample(1:m*n, round(p*m*n)))=1;
Data_M      = Data.*Omega;
Omega_trans = Omega';
Data_M_trans= Data_M';

% completion via Altenating Least Square
%   We solve Omega.*(UV)=Omega.*(Data_M)
% by solving Omega.*(Ax) = Omega.*(b), where x and v are vectors 
solve_Axb = @(A,b,Omega) A(find(Omega==1), :)\b(find(Omega==1));

% hyper parameters
res = [];
err = 1;
tot = 1e-8; 
iter = 0;
maxIter = 100;

% initialization
U = randn(m, r);
V = randn(r, n);

% Alternative Least Square
while( err >= tot && iter<=maxIter)
    for i=1:n
        V(:,i)=solve_Axb(U,Data_M(:,i),Omega(:,i));
    end
    V_trans = V';
    for j=1:m
        U(j, :)=solve_Axb(V_trans, Data_M_trans(:,j), Omega_trans(:, j))';
    end
    iter = iter + 1;
    err= norm(Omega.*(U * V-Data_M), 'fro')/norm(Omega.*(Data_M), 'fro');
    res = [res, log10(err)];
    disp(['At iteration ' num2str(iter) ' the error is ' num2str(err)]);
end

figure()
hold on
plot(res, 'linewidth',3);
xlabel('Iteration')
ylabel('Recovery Error(log10)');
hold off


