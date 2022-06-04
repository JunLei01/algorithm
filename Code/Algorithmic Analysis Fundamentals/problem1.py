
def getFile(path, nums):
    filename = []
    for i in range(0, 10):
        name = path + "COUNT" + str(i) + ".IN"
        filename.append(name)
    for i in range(len(filename)):
        f = open(filename[i], "r")
        nums.append(f.read())

def Counting(outpath, nums):
    filename = []
    for i in range(0, 10):
        name = outpath + "answer" + str(i) + ".OUT"
        filename.append(name)
    x = 0
    for num in nums:
        countNum = [0 for i in range(10)]
        Count(num, countNum)
        for i in range(0, len(num)):
            countNum[0] -= 10**i
        f = open(filename[x], "w")
        for item in countNum:
            f.write("%s\n" % item)
        x += 1

def Count(num, countNum):
    length = len(num)
    p = int(num[0])
    for i in range(10):
        countNum[i] += p * (length-1) * int(10**(length-2))
    for i in range(p):
        countNum[i] += int(10**(length-1))
    remain = int(10**(length-1))
    num = int(num)
    remain = num % remain
    if remain == 0:
        countNum[p] += 1
        countNum[0] += length - 1
        return
    remainLength = len(str(remain))
    if remainLength != length - 1:
        countNum[0] += (length-1-remainLength)*(remain + 1)
    countNum[p] += 1 + remain
    return Count(str(remain), countNum)

if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Algorithmic Analysis Fundamentals/COUNTING/TEST/"
    outpath = "D:/algorithm/Data/Algorithmic Analysis Fundamentals/COUNTING/ANSWER/"
    nums = []
    getFile(inpath, nums)
    Counting(outpath, nums)


