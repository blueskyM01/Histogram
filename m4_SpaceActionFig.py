import matplotlib.pyplot as plt
from pylab import *  # 支持中文

# mpl.rcParams['font.sans-serif'] = ['SimHei']


x = [1, 2, 3, 4, 5, 6]
y = [0.037, 0.045, 0.173, 0.211, 0.477, 0.692]
x1 = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
y1 = [0.044, 0.059, 0.215, 0.378, 0.502, 0.743]

# plt.plot(x, y, marker='o', mec='r', mfc='w')
plt.plot(x1, y1, marker='o', mec='r', mfc='w')
# plt.legend()  # 让图例生效

# plt.xlabel("step(°)")  # X轴标签
plt.xlabel("step(m/s)")  # X轴标签
# plt.ylabel("PD")  # Y轴标签
plt.ylabel("PV")  # Y轴标签
# plt.title("A simple plot")  # 标题


plt.show()
