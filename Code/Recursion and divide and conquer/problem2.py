import sys
sys.setrecursionlimit(100000)  # 设置递归深度为十万
from OperateFile.operatefile import getfile, writefile, getfiles

def f(n, m):
    if m == 1 or n == m:
        return 1
    else:
        return f(n-1, m-1)+f(n-1, m)*m

if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Recursion and divide and conquer/SET PARTITION/TEST/"
    filename = []
    filename = getfiles(inpath, "BELL", 0, 5)
    for i in range(0, 6):
        num = getfile(filename[i])
        sum = 0
        for j in range(1, num[0]+1):
            sum += f(num[0], j)
        outpath = "D:/algorithm/Data/Recursion and divide and conquer/SET PARTITION/ANSWER/"
        outpath = outpath + "answer" + str(i) + ".out"
        writefile(sum, outpath)