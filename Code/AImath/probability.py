# from scipy import stats as st
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
#
# #  规定编码格式，防止乱码
# mpl.rcParams['font.sans-serif'] = [u'SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
#
# #  二项分布
# n, p = 100, 0.25
# k = np.arange(0, n)
# binomial = st.binom.pmf(k, n, p)
# plt.plot(k, binomial, 'o-')
# plt.title('伯努利分布:n=%i, p=%.2f'%(n, p), fontsize=15)
# plt.xlabel('成功次数')
# plt.ylabel('成功概率', fontsize=15)
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import random
#  中文显示
plt.rcParams['font.sans-serif'] = ['simhei']
#  定义50轮抛硬币模拟实验
batch = 500
sanples = 500*np.ones(batch, dtype=np.int32)
result = []
result_mean = []
#  统计每次实验硬币正面朝上的概率
for _ in range(batch):
    for i in range(sanples[_]):
        result.append(random.randint(0, 1))
        result_mean.append(np.mean(result))
        xaxis = list(range(batch))
    print(len(xaxis))
    print(len(result_mean))
    plt.plot(xaxis, result_mean)
    plt.xlabel('抛硬币数')
    plt.ylabel('正面朝上的概率')
    plt.show()