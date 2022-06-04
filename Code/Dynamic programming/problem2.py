import math
import numpy as np

from OperateFile.operatefile import get_all_file, writefile, getfiles, getfile


def min_coins_num(nums, T, coins, m):
    c = [100000 for inf in range(m+1)]   # 初始化矩阵的每个值为100000
    c[0] = 0
    for i in range(nums):
        for j in range(coins[i]):
            for k in range(m, T[i]-1, -1):
                c[k] = min(c[k], c[k-T[i]]+1)
    if c[m] != 100000:
        return c[m]
    else:
        return "error"



if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Dynamic programming/COIN CHANGING/TEST/"
    filename = []
    filename = getfiles(inpath, "COINS", 0, 6)
    T = []
    coins = []
    for i in range(0, 7):
        T.clear()
        coins.clear()
        content = getfile(filename[i])
        nums = int(content[0])
        m = int(content[-1])
        for i in content[1:len(content)-1]:
            a = i.split(' ')
            T.append(int(a[0]))
            coins.append(int(a[1]))
        MIN = min_coins_num(nums, T, coins, m)
        outpath = "D:/algorithm/Data/Dynamic programming/COIN CHANGING/ANSWER/"
        outpath = outpath + "answer" + ".out"
        writefile(MIN, outpath)

