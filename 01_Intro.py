"""
A simple python script to introduce
numerical libraries, 
	
	* scikit-learn, 
	* numpy 
	* matplotlib

1. Load iris dataset 
2. Perform KMeans
3. Plot output

Mar-07-2016
Gopi Subramanian
"""

# Load Libraries
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn import datasets

# Let us use Iris dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

# Fit KMeans
model = KMeans(n_clusters = 3)
model.fit(X)

# Plot output
fig = plt.figure(1)
plt.clf()
plt.scatter(X[:,1],X[:,2],c = model.labels_)
plt.show()

