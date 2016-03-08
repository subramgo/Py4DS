"""
Split data as train and test

Mar-07-2016
Gopi Subramanian
"""

# Load Libraries
import numpy as np 
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.crossvalidation import train_test_split


# Let us use Iris dataset
iris = datasets.load_iris()
x = iris.data
y = iris.target

# Stack x and y togetehr
input_dataset = np.colstack([x,y])
train,test = train_test_split(input_dataset,test_size = 0.2)

# Perform Stratified Split data by class variable
stratified_split = StratifiedShuffleSplit(y,test_size = 0.2, n_iter = 1)

for train_indx,test_indx in stratified_split:
    train = input_dataset[train_indx]
    test =  input_dataset[test_indx]
