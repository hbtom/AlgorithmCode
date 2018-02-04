train_x = [[-1,-1],[0,0],[1,1]]
train_y = [-1,0,1]

# Lasso regression
# solve x = argmin_x 1/(2n) * || y - Ax ||_2^2 + alpha * ||x||_1  
from sklearn.linear_model import Lasso
model = Lasso(alpha=0.1)
model.fit(train_x, train_y)
print(["** Lasso **"])
print(["Model", model.coef_])
print(["Prediction", model.predict([[3, -3]])])

# Ridge regression (coefficient is more robust to collinearity)
# solve x = argmin_x || y- Ax ||_2^2 + alpha * ||x||_2^2
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.1)
model.fit(train_x, train_y)
print(["** Ridge **"])
print(["Model", model.coef_])
print(["Prediction", model.predict([[3, -3]])])

# ElasticNet
# solve x = argmin_x 1/(2n)*||y-Ax||_2^2 + alpha*rho*||x||_1 + alpha(1-rho)/2||x||_2^2 
from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=0.1)
model.fit(train_x, train_y)
print(["** ElasticNet **"])
print(["Model", model.coef_])
print(["Prediction", model.predict([[3, -3]])])

#KNN
# Brutal force: O(dN) to find the neighbor for one testing data
# Tree apporach: O(dNlog*(N)), intuited from if A is far from C, B is close to A, then B is far from C
# KD-Tree: build tree along axis, which is fast in building the tree and taking O(log(N)) to classify data, but weak when d is large
# Ball-Tree: group points to balls centered at Ci with radius ri, and testing is only performs between data center and testing data
train_x = [[-1, -2], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]
from sklearn.neighbors import NearestNeighbors
import numpy as np 
model = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(train_x)
distances, indices = model.kneighbors([[0,0]])
print(["** KNN **"])
print(indices)
print(distances)

# LogisticRegression
train_x = [[-2,-3],[1,0],[1,1]]
train_y = [1,0,1]
from sklearn.linear_model import LogisticRegression
import numpy as np
model = LogisticRegression(penalty="l2")
model.fit(train_x, train_y)
print(["** Logistic Regression **"])
print(model.coef_)
print(model.predict([[3,3]]))

# SVM 
train_x = [[-3,-2],[-4,-5],[3,4],[4,5]]
train_y = [1,1,2,2]
from sklearn.svm import SVC
import numpy as np
model = SVC()
model.fit(train_x,train_y)
print(["** SVC **"])
print(model.predict([[0,0]]))

# K-Means
train_x = [[-3,-2],[-4,-5],[3,4],[4,5]]
from sklearn.cluster import KMeans 
import numpy as np 
model = KMeans(n_clusters=2, random_state=0).fit(train_x)
print('** KMeans **')
print(model.labels_)
print(model.predict([[1,2],[-1,-1]]))
print(model.cluster_centers_)

# PCA
train_x = [[-3,-2],[-4,-5],[3,4],[4,5]]
from sklearn.decomposition import PCA
import numpy as np 
model = PCA(n_components=2)
model.fit(train_x)
print(model.explained_variance_ratio_)















