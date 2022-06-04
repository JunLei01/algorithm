import math
import numpy as np

from OperateFile.operatefile import get_all_file, writefile, getfiles

def oiling_car(nums, arr):
    for i in arr:
        if i > int(nums[0]):
            return "No Solution"
    MIN = 0
    all_length = arr[0]
    for i in range(1, int(nums[1])):
        all_length += arr[i]
        if all_length + arr[i+1] > int(nums[0]):
            MIN += 1
            all_length = 0
    return MIN

if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Greedy algorithm/OILING CAR/TEST/"
    filename = []
    filename = getfiles(inpath, "OIL", 0, 11)
    for i in range(0, 11):
        nums, arr = get_all_file(filename[i])
        nums = nums.split(' ')
        MIN = oiling_car(nums, arr)
        outpath = "D:/algorithm/Data/Greedy algorithm/OILING CAR/ANSWER/"
        outpath = outpath + "answer" + str(i) + ".out"
        writefile(MIN, outpath)

