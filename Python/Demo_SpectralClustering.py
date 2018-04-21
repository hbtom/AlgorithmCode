#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:19:39 2018
Reference: https://papers.nips.cc/paper/2092-on-spectral-clustering-analysis-and-an-algorithm.pdf
@author: wenqiwang
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

# Data: N x d
n, d, k = 100, 2, 3
Data = normalize(np.random.randn(n, d), norm='l2', axis=1)
Data = np.concatenate([Data, 5 * normalize(np.random.randn(2*n, d), norm='l2', axis=1)], 0)
Data = np.concatenate([Data, 10 * normalize(np.random.randn(2*n, d), norm='l2', axis=1)], 0)
plt.scatter(Data.transpose()[0], Data.transpose()[1], color='k')

# Spectral clustering algorithm
sigma = 1.0
# step1: affinity matrix
# computation:O(N^2d)
N = np.shape(Data)[0]
A = np.zeros([N, N])
for i in range(N):
    for j in range(N):
        if(i != j):
            A[i][j] = np.exp(-np.square(np.linalg.norm(Data[i]-Data[j]))/(2*np.square(sigma)))

# step2: laplace matrix: 
# computation: O(N^2)
D_half = np.diag(np.sqrt(1.0/np.sum(A, 1)))
L = np.matmul(np.matmul(D_half, A), D_half)

# step3: find X: N x k, which is k largest eigenvectors of L
# computation: O(N^2)
val, vec = np.linalg.eig(L)
X =  normalize(vec[:,range(k)], axis=1)

# step3: k-means
# computation: O()
from sklearn.cluster import KMeans
model = KMeans(n_clusters=k)
model.fit(X)
labels = model.predict(X)
plt.scatter(Data[labels==0].transpose()[0], Data[labels==0].transpose()[1], color='r')
plt.scatter(Data[labels==1].transpose()[0], Data[labels==1].transpose()[1], color='g')