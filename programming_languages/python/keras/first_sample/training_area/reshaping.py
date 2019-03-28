import numpy as np
from random import randint

lis = [x for x in range(10)]
np_arr = np.array(lis)

# print(np_arr.reshape(2,5))
# print(np_arr)
# print(np_arr.reshape(-1,1))

# valid_set = np.array([randint(13, 64) for x in range(95)]).reshape(-1,1)
# print(valid_set)

v_young = [randint(13, 64) for x in range(95)]
l_young = [0 for _ in range(95)]
v_old = [randint(65, 100) for x in range(95)]
l_old = [1 for _ in range(95)]
v_y = [randint(13, 64) for x in range(5)]
l_y = [0 for _ in range(5)]
v_ = [randint(65, 100) for x in range(5)]
l_ = [0 for _ in range(5)]

valid_set = []
valid_set.append(v_young)
valid_set.append(v_y)
valid_set.append(v_old)
valid_set.append(v_)
print(np.array(valid_set).reshape(-1,1))