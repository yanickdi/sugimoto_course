import matplotlib.pyplot as plt
import numpy as np
import sys

x = np.arange(-2 , 20, 0.001)
y = np.empty(len(x))
for i, x_val in enumerate(x):
    if x_val < 0:
        y[i] = 0
    else:
        y[i] = 1 - 1/(1+ x_val**2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, label='f(x)')

#ax.set_aspect('equal')
plt.legend()
plt.ylim(-.5, 1.5)
plt.xlim(-2, 20)
plt.grid()
plt.show()