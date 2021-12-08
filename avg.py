import numpy as np

np.random.seed(0) #シードを固定(randomで出る値が同じになる)
rs = []

# for n in range(1,11):
#     r = np.random.rand() #ダミーの報酬
#     rs.append(r)
#     q = sum(rs)/n
#     print(q)
#これでは、nが大きくなった時にrsのメモリが増えるのと、sumの計算量が増えてしまう

q = 0
#改善
for n in range(1,11):
    r = np.random.rand()
    q = q + (r - q)/n
    # q += (r - q)/n　でもよい
    print(q)


