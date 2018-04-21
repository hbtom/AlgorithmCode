#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 01:38:48 2018
@author: wenqiwang
Reference: http://benalexkeen.com/k-means-clustering-in-python/
"""

import numpy as np
import matplotlib.pyplot as plt 

# generate data
n, s, k = 200,5, 4
eps     = 10**-3
maxiter = 100
itr     = 0
err     = 1
Data = [np.random.randn(n)+s, np.random.randn(n)+s]
Data = np.concatenate( [Data,[np.random.randn(n)-s, np.random.randn(n)+s]], 1)
Data = np.concatenate( [Data,[np.random.randn(n)-s, np.random.randn(n)-s]], 1)
Data = np.concatenate( [Data,[np.random.randn(n)+s, np.random.randn(n)-s]], 1)
plt.scatter(Data[0], Data[1], color='k')
Data = np.transpose(Data)   # N * d
#plt.scatter([d,d,-d,-d], [d,-d,d,-d], color='r')

# iniitalization
def Kmeans_ini(Data, k, method='random'):
    # Data: N x d
    # C:    k x d
    N = np.shape(Data)[0]
    if method=='random':
        idx = [np.random.randint(0, N) for i in range(k)]
        C   = [[Data[i][0],Data[i][1]] for i in idx]
    return np.array(C)
# assign label
# computation: O(Ncd)
def Kmeans_AssignLabe(Data, C):
    # input:    Data: N x d
    #           C:    k x d
    # output:   y:    N x 1
    dist = np.array([[np.linalg.norm(a-c) for c in C] for a in Data])
    #dist = np.transpose([np.sqrt((Data.transpose()[0]-c[0])**2 +(Data.transpose()[1] - c[1])**2) for c in C])
    y    = np.argmin(dist, 1)
    return y
# update center
# computation: O(Nd)
def Kmeans_UpdateCenter(Data, y, k):
    # input:  Data: N x d
    #         y:    N x 1
    # output: C:    k x d
    return np.array([np.mean(Data[y==i], 0) for i in range(k)])


# iteration over the solver
C_pre = Kmeans_ini(Data, k)
while(itr < maxiter and err >= eps ):
    y = Kmeans_AssignLabe(Data, C_pre)
    C = Kmeans_UpdateCenter(Data, y, k)
    err = np.linalg.norm(C-C_pre)
    itr=itr+1
    C_pre = C
# plot results    
print("Total iteration is ", itr)
print("Learnt centers: ", C)
plt.scatter(C.transpose()[0], C.transpose()[1], color='r')

# pakage solver
from sklearn.cluster import KMeans
model = KMeans(n_clusters=k)
model.fit(Data)
centroids = model.cluster_centers_
print("Package learnt centers: ", centroids)
plt.scatter(centroids.transpose()[0], centroids.transpose()[1], color='g')


        
        
    


