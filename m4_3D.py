# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:17:13 2015

@author: Eddy_zheng
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(4, 11, 1)
Y = np.arange(100, 400, 50)
X, Y = np.meshgrid(X, Y)

# print(X)
# print(Y)
#
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# print(Z)

Z = np.array([[64.24, 54.29, 30.75, 30.16, 20.45, 19.78, 10.54], [59.23, 48.23, 20.49, 19.88, 12.46, 9.36, 5.469],
              [50.74, 40.18, 11.93, 10.27, 4.33, 4.21, 3.13],
              [44.96, 33.72, 9.14, 5.87, 3.27, 2.13, 2.06], [39.58, 29.53, 6.23, 4.09, 2.03, 2.04, 1.98],
              [35.23, 25.2, 5.98, 3.99, 2.02, 1.94, 1.90]])

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
