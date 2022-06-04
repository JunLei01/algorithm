import math

from OperateFile.operatefile import getfile, writefile, getfiles

def f(x):
    return 3*x
def g(x):
    return math.floor(x/2)

def dfs(n, m, deepth, operate):
    if deepth > 25:
        return False
    temp = n
    for i in range(0, 2):
        if i == 0:
            temp = f(n)
        else:
            temp = g(n)
        if temp == m or dfs(temp, m, deepth+1, operate):
            if i == 0:
                operate.append('f')
            else:
                operate.append('g')
            return True
    return False


def transformation(n, m):
    min_length = []
    operate = []
    final = []
    if dfs(n, m, 1, operate):
        min_length.append(len(operate))
        final.append(operate)
    return len(operate), operate

if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Backtracking/INTEGER TRANSFORMATION/TEST/"
    filename = []
    filename = getfiles(inpath, "FUNC", 0, 11)
    for i in range(0, 1):
        answer = []
        nums = getfile(filename[i])
        nums = nums[0].split(' ')
        minlength, operate = transformation(int(nums[0]), int(nums[1]))
        answer.append(minlength)
        answer.append(operate)
        outpath = "D:/algorithm/Data/Backtracking/INTEGER TRANSFORMATION/ANSWER/"
        outpath = outpath + "answer" + str(i) + ".out"
        writefile(answer, outpath)
