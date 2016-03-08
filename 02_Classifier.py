"""
A simple python script to introduce
numerical libraries, 
	
	* scikit-learn, 
	* numpy 
	* matplotlib

1. Load iris dataset 
2. Perform Classification

Mar-07-2016
Gopi Subramanian
"""

# Load Libraries
import numpy as np 
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Let us use Iris dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target

# Build a classifier
estimator = DecisionTreeClassifier()
estimator.fit(x,y)
predicted_y = estimator.predict(x)

# Find model accuracy
print "Model accuracy = %0.2f"%(accuracy_score(y,predicted_y) * 100) + "%\n"
    