from matplotlib import pyplot as plt
import numpy as np

circle_radius = 5
num_points = 1024

t = np.linspace(0, 2 * np.pi, num_points + 1)

x = circle_radius * np.cos(t)
y = circle_radius * np.sin(t)

def f(X):
    eq = X/2
    return eq


plt.axis("equal")
plt.grid()
plt.plot(x, y)
linearxset = np.arange(-50, 50, 0.1)
linearvalues = np.sin(linearxset)

plt.plot(linearxset, f(linearvalues))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
