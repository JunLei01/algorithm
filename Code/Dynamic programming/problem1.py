import math
import numpy as np

from OperateFile.operatefile import get_all_file, writefile, getfiles

def merging_of_stones(nums, arr):
    MAX, MIN = 0, 0
    Min = np.full((100, 100), 000, dtype=int)
    Max = np.full((100, 100), 0, dtype=int)
    sum = np.full(nums*2+1, 0, dtype=int)
    for i in range(0, nums):
        arr.append(arr[i])
    for i in range(1, nums*2+1):
        sum[i]=sum[i-1]+arr[i-1]
    for length in range(2, nums+1):
        l = 1
        while(length+l-1 <= 2*nums):
            r = length + l - 1
            Min[l][r] = 10000
            for k in range(l, r):
                Min[l][r] = min(Min[l][r], Min[l][k] + Min[k + 1][r] + sum[r] - sum[l - 1])
                Max[l][r] = max(Max[l][r], Max[l][k] + Max[k + 1][r] + sum[r] - sum[l - 1])
                MAX, MIN = Max[l][r], Min[l][r]
            l += 1
    return MIN, MAX


if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Dynamic programming/PEBBLE MERGING/test_and_output/"
    filename = []
    answer = []
    filename = getfiles(inpath, "MERGE", 0, 10)
    for i in range(0, 10):
        nums, arr = get_all_file(filename[i])
        MIN, MAX = merging_of_stones(nums, arr)
        answer.append(MIN, MAX)
        outpath = "D:/algorithm/Data/Dynamic programming/PEBBLE MERGING/test_and_output/"
        outpath = outpath + "answer" + str(i) + ".out"
        writefile(answer, outpath)

