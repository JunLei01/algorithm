import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

print("请输入投点次数：")
n = eval(input());
x = np.random.uniform(-1,1,n)
y = np.random.uniform(-1,1,n)

d = np.sqrt(x**2+y**2)

res = sum(np.where(d<=1.0,1,0))

pi = 4.0*res/n
print("蒙特卡洛方法所估计的pi值为：")
print(round(pi,6))

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x,y,'ro',markersize=1)
plt.axis('equal')
circle = Circle(xy=(0.0, 0.0),radius=1.0,alpha=0.5)
axes.add_patch(circle)
plt.show()