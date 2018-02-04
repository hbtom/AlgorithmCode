function x = lasso_admm(A, b, lambda)
    % solve 1/2 || Ax-b ||_2^2 + lambda || x ||_1
    
    % hyper_parameters
    tau = 1;
    Itr_max = 50;
    
    % initialization
    d = size(A,2);
    z = randn(d,1);
    y = randn(d,1);
    tp1 = inv(A' * A+ 1/tau * eye(d));
    tp2 = A' * b;
    S   = @(x, a) sign(x) .* max(abs(x)-a, 0);
    
    % updating
    for i = 1: Itr_max
        x = tp1 *(tp2 + 1/tau *(z-y));
        z = S(x+y, lambda * tau);
        y = y + 1/tau*(x-z);
    end
end