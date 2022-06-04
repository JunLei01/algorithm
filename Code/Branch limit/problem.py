import math
from OperateFile.operatefile import get_all_file, writefile, getfiles
global min_length
min_length = 0
global bestr
bestr = []
global center_postion
center_postion = [0]*20

def calculate_center(num, r):
    temp = 0
    for i in range(num):
        x_postion = center_postion[i] + 2*math.sqrt(r[num]*r[i])
        if x_postion>temp:
            temp = x_postion
    return temp

def calculate_length(r):
    global min_length
    global bestr
    low, high = 0, 0
    global center_postion
    for i in range(len(r)):
        if center_postion[i]-r[i]<low:
            low = center_postion[i]-r[i]
        if center_postion[i]+r[i]>high:
            high = center_postion[i]+r[i]
    if high-low < min_length:
        min_length = high - low
        bestr = r

def search(number, r, num):
    global center_postion
    if num == number:
        calculate_length(r)
        return 0
    else:
        for i in range(num, number):
            r[num], r[i] = r[i], r[num]
            center = calculate_center(num, r)
            global min_length
            if center+r[num]+r[1]<min_length:
                center_postion[num] = center
                search(number, r, num+1)
            r[num], r[i] = r[i], r[num]

if __name__ == "__main__":
    inpath = "D:/algorithm/Data/Branch limit/CIRCLE PERMUTATION/TEST/"
    filename = []
    filename = getfiles(inpath, "CIRCLE", 0, 11)
    for j in range(0, 11):
        min_length = 100000
        number, r = get_all_file(filename[j])
        search(int(number), r, 0)
        answer = min_length
        outpath = "D:/algorithm/Data/Branch limit/CIRCLE PERMUTATION/ANSWER/"
        outpath = outpath + "answer" + str(j) + ".out"
        writefile(answer, outpath)

