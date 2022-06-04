import math
from OperateFile.operatefile import getfile, writefile, getfiles

#  快速排序
def quick_sort(numbers, i, j):
    if i >= j:
        return numbers
    flag = numbers[i]
    low = i
    high = j
    while i < j:
        while i < j and numbers[j] >= flag:
            j -= 1
        numbers[i] = numbers[j]
        while i < j and numbers[i] <= flag:
            i += 1
        numbers[j] = numbers[i]
    numbers[j] = flag
    quick_sort(numbers, low, i-1)
    quick_sort(numbers, i+1, high)
    return numbers

def split(arr, length):
    #  以中间数字为界，确定左右界
    mid = math.ceil(length / 2)
    for left in range(0, mid+1):   # 找左界
        if arr[left] == arr[mid]:
            break
    for right in range(mid+1, length):  # 找右界
        if arr[right] != arr[mid]:
            break
    return left, right

def get_mode(mode, arr, length):
    mid = math.ceil(length/2)
    left, right = split(arr, length)
    # print(right, left, mid, maxnum, mode)
    s = right - left
    if(s > mode[1]):
        #  如果中间数字的个数大于现在的重数，更新众数和重数
        mode[0] = arr[mid]
        mode[1] = s
    if(s == mode[1]):
        #  如果出现多个众数，找最小的那个
        if mode[0] > arr[mid]:
            mode[0] = arr[mid]
            mode[1] = s
    if(left+1 > mode[1]):
        #  如果左边的个数>重数，搜索左边的
        get_mode(mode, arr, left+1)
    if(length-right > mode[1]):
        #  如果右边的个数>重数，搜索右边的
        get_mode(mode, arr[right:length], length-right)

if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Recursion and divide and conquer/MAJORITY/TEST/"
    filename = []
    filename = getfiles(inpath, "MODE", 1, 10)
    for i in range(0, 10):
        nums = getfile(filename[i])
        arr = nums[1:nums[0]+1]
        quick_sort(arr, 0, len(arr) - 1)    # 先对数组做一个快速排序
        mode = [0, 0]
        get_mode(mode, arr, len(arr))
        outpath = "D:/algorithm/Data/Recursion and divide and conquer/MAJORITY/ANSWER/"
        outpath = outpath + "answer" + str(i) + ".out"
        writefile(mode, outpath)
