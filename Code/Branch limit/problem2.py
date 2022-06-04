#-*- coding : utf-8-*-
# coding:unicode_escape
import numpy as np
from queue import Queue
global path, PathLen1
PathLen1 = 0  # 用于保存路线长度
path = []  # 保存路线
###   声明position类存放当前点的横纵坐标
class Position(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

def FindPath(start, finish, n, m, grid):  # 起始点，结束点，路径长，路径
    global path, PathLen1
    if start.row == finish.row and start.col == finish.col:
        Pathlen = 0
        return True
    grid[0, 0:m + 1] = grid[n + 1, 0:m + 1] = 1  # 设置四周的围墙
    grid[0:n + 1, 0] = grid[0:n + 1, m + 1] = 1
    offset = [Position(0, 1), Position(1, 0), Position(0, -1), Position(-1, 0)]  # 右，下，左，上
    NumofNbers = 4
    here = start
    nbr = Position(0, 0)
    grid[start.row][start.col] = 2
    Q = Queue(maxsize=0)  # 创建一个队列
    while True:
        for i in range(NumofNbers):  # 当前点的四周的点
            nbr.row = here.row + offset[i].row
            nbr.col = here.col + offset[i].col
            if grid[nbr.row, nbr.col] == 0:  # 该方格未被标记
                grid[nbr.row, nbr.col] = grid[here.row, here.col] + 1
                if nbr.row == finish.row and nbr.col == finish.col:  # 完成布线直接结束循环
                    break
                nbr1 = Position(nbr.row, nbr.col)
                Q.put(nbr1)  # 将当前点加入队列
        if nbr.row == finish.row and nbr.col == finish.col:  # 完成布线结束循环
            break
        if Q.empty():  # 队列为空，表示无解
            return False
        here = Q.get()  # 下一个拓展结点
    Pathlen = grid[finish.row, finish.col] - 2
    PathLen1 = Pathlen
    here = finish
    for j in range(Pathlen - 1, -1, -1):  # 回溯寻找路径
        path.append(Position(here.row, here.col))  # 将当前点加入路径
        for i in range(NumofNbers):
            nbr.row = here.row + offset[i].row
            nbr.col = here.col + offset[i].col
            if grid[nbr.row, nbr.col] == j + 2:  # 找到上一个坐标
                break
        here = Position(nbr.row, nbr.col)  # 更新为上一个坐标
    return True

def main():
    global path, PathLen1
    n, m = 7, 7     #  m,n表示方阵的行数和列数
    grid = np.zeros((n + 2, m + 2), dtype=int)   #  初始化方阵
    #   输入方阵的值
    for i in range(1, n + 1):
        grid[i, 1:n + 1] = np.array(input().split(), dtype=int)

    start_x, start_y = 3, 2        #   起点的坐标
    finish_x, finish_y = 4, 6        #    终点的坐标
    start = Position(start_x, start_y)
    finish = Position(finish_x, finish_y)
    if FindPath(start, finish, n, m, grid):
        print("Path length: ", PathLen1)
        path.append(start)
        path = np.flipud(path)
        print("The way to move is as follows:")
        for i in range(len(path) - 1):
            print("(", path[i+1].col - path[i].col, ",", path[i+1].row - path[i].row, ")", end="  ")
    else:
        print("No path!")



if __name__ == '__main__':
    main()


