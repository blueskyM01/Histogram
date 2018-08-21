import matplotlib.pyplot as plt
import heapq
import numpy as np

test_list = [2791, 1152, 282, 47, 23, 81, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0]

maxnum_3 = map(test_list.index, heapq.nlargest(3, test_list))
maxnum_3_index = list(maxnum_3)

max1 = test_list[maxnum_3_index[0]]
max2 = test_list[maxnum_3_index[1]]
max3 = test_list[maxnum_3_index[2]]

max1_duo = int(max1 / 1.4)
max2_duo = int(max2 / 6)
max3_duo = int(max3 / 6)

sumduo = max1_duo + max2_duo + max3_duo
print("sumduo:",sumduo)
test_list[maxnum_3_index[0]] = max1 - max1_duo
test_list[maxnum_3_index[1]] = max2 - max2_duo
test_list[maxnum_3_index[2]] = max3 - max3_duo

cccc = test_list[2:40]
cccclist = []
already = 0
for i in range(len(cccc)):
    ra = np.random.randint(5, (sumduo - already)/5 - (len(cccc) - i), 1, dtype='l')
    cccclist.append(ra[0])
    already =already+ra
cccclist.append((sumduo - already)[0])

print("sum:",sum(cccclist))
print(cccclist)
for ii, jj in zip(range(2, 40), cccclist):
    test_list[ii] = test_list[ii] + jj

print(test_list)

plt.bar([x / 10 for x in range(len(test_list))], test_list, 0.1)
plt.show()
# plt.savefig("test")
