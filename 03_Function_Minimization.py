"""
Function minimiztion using
scipy

Mar-07-2016
Gopi Subramanian
"""

from scipy import optimize
import numpy as np 
import matplotlib.pyplot as plt 

# Define a function
def afunction(x):
	return -np.exp(-(x-.7)**2)

# Generate some input
vals = np.arange(-5,5,0.5)
fvals =[afunction(x) for x in vals]

# Plot the function
plt.figure(2)
plt.plot(fvals)

plt.show()

print optimize.brent(afunction)

#Alternatively
print optimize.minimize_scalar(afunction)