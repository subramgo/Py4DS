"""
A simple python script to introduce
numerical libraries, 
	
	* scikit-learn, 
	* numpy 
	* matplotlib

1. Load iris dataset 
2. Perform Classification
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

# Combine and shuffle them
X_all = np.column_stack([X,Y])
np.random.shuffle(X_all)

# Train test split of data
# We need  80/20 split.
# 80% of our records for Training
# 20% Remaining for our Test set
train,test = train_test_split(X_all,test_size=0.2)
