import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from scipy.stats import gaussian_kde

np.random.seed(42)
data1=np.concatenate([
    np.random.normal(4,0.3,50),
    np.random.normal(7,0.4,50)
])
kde1=gaussian_kde(data1[:50])
kde2=gaussian_kde(data1[50:])
x_vals=np.linspace(min(data1)-1,max(data1)+1,100)
plt.figure(figsize=(10,8))
plt.plot(x_vals,kde1(x_vals),label='X',color='red')
plt.plot(x_vals,kde2(x_vals),label='y',color='yellow')
plt.scatter(data1,np.zeros_like(data1),color='green')
plt.title("Clustering")
plt.show()
scores=[]
X, _=make_blobs(n_samples=200,centers=3,n_features=2,random_state=42)
K=range(1,5)
for k in K:
    kmeans=KMeans(n_clusters=k,n_init=10,max_iter=100,random_state=42)
    kmeans.fit(X)
    scores.append(-kmeans.inertia_)
plt.figure(figsize=(8,4))
plt.plot(K,scores,color='green')
plt.grid()
plt.title("elbow curve")
plt.show()
    
