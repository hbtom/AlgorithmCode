import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

N, k = 1000, 2
b0 = np.ones([N,1])
x0 = np.sort(np.random.randn(N,k)*10, axis=0)
X0 = np.concatenate((b0,x0), axis=1)
beta0 = np.random.rand(k+1, 1)
y0 = np.matmul(X0, beta0)
y = y0 + np.random.randn(N, 1) *  5

# pseudo-inverse solver
beta_predict = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X0),X0)), np.transpose(X0)), y)
# pseudo-inverse solver partition
X0TX0 = np.add(np.matmul(np.transpose(X0[range(N/2),:]),X0[range(N/2),:]),\
               np.matmul(np.transpose(X0[range(N/2, N),:]),X0[range(N/2, N),:]))
beta_predict2 = np.matmul(np.matmul(np.linalg.inv(X0TX0), np.transpose(X0)), y)


# stats solver
model = sm.OLS(y,X0).fit()
print(model.summary())

# plot 
if k==1:
    plt.scatter(x0, y)
    plt.plot(x0, np.matmul(X0, beta_predict), 'r')

# Display
print('ground truth: \n', beta0)
print('precdict: \n ', beta_predict)
print('precdict2: \n ', beta_predict2)


