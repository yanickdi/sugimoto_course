import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_dist(ax, x, y):
    ax.plot([0, x], [0, y])
    dist = (x**2 + y**2)**(1/2)
    dist_str = 'd = {:.2f}'.format(dist)
    #ax.text(x/2, y/2, dist_str)
    ax.text(x, y, '({:.1f}/{:.1f}), {}'.format(x, y, dist_str))

x = np.arange(0,1.001, 0.001)
y = np.sqrt(1-x**2)
points = [0.6, 0.1,   0.2, 0.7,  0.9, 0.6, 0.4, 0.5]
points_x = [p for i, p in enumerate(points) if i % 2 == 0]
points_y = [p for i, p in enumerate(points) if i % 2 == 1]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, label='$x^2 + y^2 = 1$')
ax.plot(points_x, points_y, linestyle='', marker='o', label='ZZ')
plot_dist(ax, points_x[0], points_y[0])
plot_dist(ax, points_x[1], points_y[1])
plot_dist(ax, points_x[2], points_y[2])
plot_dist(ax, points_x[3], points_y[3])
ax.set_aspect('equal')
plt.legend()
plt.ylim(0, 1.1)
plt.xlim(0, 1.1)
plt.grid()
#plt.show()
plt.savefig(sys.argv[0].replace('.py', '.pdf'))