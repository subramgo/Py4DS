"""
Introducing Matplotlib
Mar-07-2016
Gopi Subramanian
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')
# Sample x y data for line and simple dot plots
x = np.arange(1,100,dtype=float)
y = np.array([np.power(xx,2) for xx in x])

# Line Plot
plt.figure(1)
plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Line Plot')

# Dot plot
plt.figure(2)
plt.plot(x,y,'or')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Dots')

# Sample x,y data for scatter plot
x = np.random.uniform(size=100)
y = np.random.uniform(size=100)
labels = np.random.randint(2,size=100)

# Scatter plot
plt.figure(3)
plt.scatter(x,y,c=labels)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Scatter with color')

plt.show()


