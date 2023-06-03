#this script was generated with GPT4
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for Möbius strip
theta = np.linspace(0, 2.0 * np.pi, 100)
w = np.linspace(-0.25, 0.25, 25)
w, theta = np.meshgrid(w, theta)

# Parametrize the Möbius strip
phi = 0.5 * theta
r = 1 + w * np.cos(phi)
x = np.cos(theta) * r
y = np.sin(theta) * r
z = w * np.sin(phi)

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, color='c', rstride=5, cstride=5)

# Display the plot
plt.show()
