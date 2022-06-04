from OperateFile import operatefile
#  以i开头长度为k的升序字符串的总个数
def dfs(i, k):
    sum = 0
    if k == 1:
        return 1
    for j in range(i + 1, 27):
        sum += dfs(j, k - 1)
    return sum


def fun(k):
    sum = 0
    for i in range(1, 27):
        sum += dfs(i, k)
    return sum


def run(inpath, outpath):
    string = operatefile.getfile(inpath)
    result = []
    for s in string:
        if s == string[0]:
            continue
        ans, l, temp = 1, len(s), 0
        for i in range(1, l):
            ans += fun(i)
        for i in range(l):
            num = ord(s[i]) - ord('a') + 1
            len2 = l - i
            for j in range(temp + 1, num):
                ans += dfs(j, len2)
            temp = num
        result.append(ans)
    operatefile.writefile(result, outpath)


if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Algorithmic Analysis Fundamentals/DICTIONARY/TEST/ENCODE.IN"
    outpath = "D:/algorithm/Data/Algorithmic Analysis Fundamentals/DICTIONARY/ANSWER/answer.OUT"
    run(inpath, outpath)