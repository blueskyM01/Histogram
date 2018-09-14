import matplotlib.pyplot as plt
import heapq
import numpy as np

test_list = [1116, 2020, 1722, 1027, 462, 229, 123, 135, 260, 176, 64, 78, 18, 81, 98, 74, 7, 84, 76, 74, 35, 67, 11,
             15, 13, 22, 35, 13, 7, 33, 37, 11, 14, 49, 24, 36, 47, 37, 20, 40, 31, 34, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1,
             0, 0, 1]

plt.bar([x / 10 for x in range(len(test_list))], test_list, 0.1)
plt.show()
