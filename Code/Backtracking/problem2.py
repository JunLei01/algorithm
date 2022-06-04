import math
from OperateFile.operatefile import get_all_file, writefile, getfiles
array = []
step = 0
operator = ['+', '-', '*', '/']
A = []
result = []

def func(num, i, operate):
    if operate == '+':
        return num + i
    if operate == '-':
        return num - i
    if operate == '*':
        return num * i
    if operate == '/':
        return num / i

def dfs(num, deepth, now_deepth, m, calcultion):
    now_deepth += 1             #  每递归一次深度+1
    if now_deepth >= deepth:    #  判断是不是最深的子节点（即是不是最后一个数）
        return False
    global step                 #  记录当前的计算步数
    if now_deepth >= step:      #  判断当前的步数是否超过最小步数
        return False
    global flag, A
    for i in A[now_deepth:flag+int(deepth)]:
        for j in operator:
            temp = func(num, i, j)          #  计算当前的值
            calcultion.append(j)                #  获取当前符号
            calcultion.append(i)            #  获取当前数字
            if temp == m or dfs(temp, deepth, now_deepth, m, calcultion):
                global result
                result.clear()
                step = now_deepth
                result.append(step)
                for i in calcultion:
                    result.append(i)
            calcultion.pop()                #  如果当前的符号得不出结果，将当前符号从符号列表中删除，遍历下一个符号
            calcultion.pop()                #  如果当前的数字得不出结果，将当前数字从数字列表中删除，遍历下一个数字
    return False

def transformation(n, m):
    print(n, m, array)
    deepth = len(array)   #  由于每个数只能
    global step
    step = deepth         #  最小步数初始化
    now_deepth = 0        #  当前树的深度
    calcultion = []
    for i in array:
        calcultion.clear()   #  每开启一轮新的遍历就将运算符列表初始化为空
        global flag
        flag = array.index(i)
        calcultion = [i]
        dfs(i, deepth, now_deepth, m, calcultion)      #   深搜遍历每个节点每种运算
        del(A[0])



if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Backtracking/COMPUTATION WITHOUT PRIORITY/TEST/"
    filename = []
    filename = getfiles(inpath, "ARIT", 0, 11)
    for j in range(0, 11):
        result.clear()
        answer = []
        array.clear()
        A.clear()
        nums, array = get_all_file(filename[j])
        n = nums.split(" ")[0]
        m = nums.split(" ")[1].split("\n")
        for i in range(0, int(n)):
            A.append(array[i])
        for i in range(0, int(n)):
            A.append(array[i])
        transformation(int(n), int(m[0]))
        if not len(result):
            result = ["No solution!"]
        else:
            R = [str(i) for i in result[1:]]
            R = ''.join(R)
            answer.append(result[0])
            answer.append(R)
            print(result)
            outpath = "D:/algorithm/Data/Backtracking/COMPUTATION WITHOUT PRIORITY/ANSWER/"
            outpath = outpath + "answer" + str(j) + ".out"
            writefile(answer, outpath)