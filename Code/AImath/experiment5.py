import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import  Rbf
from matplotlib import cm
plt.rcParams['axes.unicode_minus']=False

x = np.random.rand(100) * 4.0 -2.0
y = np.random.rand(100) * 4.0 -2.0
z = x * np.exp(-x ** 2 - y ** 2)

rf = Rbf(x, y, z,epsilon = 2)
ti = np.linspace(-2.0, 2.0, 34)
xi, yi = np.meshgrid(ti, ti)
zi = rf(xi, yi)

plt.figure()
ax1 = plt.subplot2grid((1,2), (0,0), projection='3d')
ax1.scatter(x, y, z, color = 'r')
ax2 = plt.subplot2grid((1,2), (0,0), projection='3d')
ax2.scatter(xi, yi, zi,color = 'c')
plt.tight_layout()
plt.show()
