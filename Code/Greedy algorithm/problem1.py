import math
import numpy as np

from OperateFile.operatefile import get_all_file, writefile, getfiles

def optimal_merge(nums, arr):
    arr1 = []
    for i in arr:
        arr1.append(i)
    MIN, MAX = 0, 0
    tem1, tem2 = 0, 0
    for i in range(0, nums):
        tem1 += arr[i]
        del arr[0: 1]
        arr.append(tem1)
        arr.sort()
        MIN += tem1
    for i in range(nums-1, -1, -1):
        tem2 += arr1[i]
        MAX += tem2
    MIN = MIN - arr[0]
    MAX = MAX - arr1[nums-1] - nums + 1
    return MIN, MAX



if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Greedy algorithm/OPTIMAL MERGE/TEST/"
    filename = []
    answer = []
    filename = getfiles(inpath, "MERGE", 0, 11)
    for i in range(0, 11):
        answer.clear()
        nums, arr = get_all_file(filename[i])
        arr.sort()
        MIN, MAX = optimal_merge(nums, arr)
        answer.append(MIN)
        answer.append(MAX)
        outpath = "D:/algorithm/Data/Greedy algorithm/OPTIMAL MERGE/ANSWER/"
        outpath = outpath + "answer" + str(i) + ".out"
        writefile(answer, outpath)

