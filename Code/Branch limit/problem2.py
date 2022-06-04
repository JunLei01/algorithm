#-*- coding : utf-8-*-
# coding:unicode_escape
import numpy as np
from queue import Queue
global path, PathLen1
PathLen1 = 0  # ���ڱ���·�߳���
path = []  # ����·��
###   ����position���ŵ�ǰ��ĺ�������
class Position(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

def FindPath(start, finish, n, m, grid):  # ��ʼ�㣬�����㣬·������·��
    global path, PathLen1
    if start.row == finish.row and start.col == finish.col:
        Pathlen = 0
        return True
    grid[0, 0:m + 1] = grid[n + 1, 0:m + 1] = 1  # �������ܵ�Χǽ
    grid[0:n + 1, 0] = grid[0:n + 1, m + 1] = 1
    offset = [Position(0, 1), Position(1, 0), Position(0, -1), Position(-1, 0)]  # �ң��£�����
    NumofNbers = 4
    here = start
    nbr = Position(0, 0)
    grid[start.row][start.col] = 2
    Q = Queue(maxsize=0)  # ����һ������
    while True:
        for i in range(NumofNbers):  # ��ǰ������ܵĵ�
            nbr.row = here.row + offset[i].row
            nbr.col = here.col + offset[i].col
            if grid[nbr.row, nbr.col] == 0:  # �÷���δ�����
                grid[nbr.row, nbr.col] = grid[here.row, here.col] + 1
                if nbr.row == finish.row and nbr.col == finish.col:  # ��ɲ���ֱ�ӽ���ѭ��
                    break
                nbr1 = Position(nbr.row, nbr.col)
                Q.put(nbr1)  # ����ǰ��������
        if nbr.row == finish.row and nbr.col == finish.col:  # ��ɲ��߽���ѭ��
            break
        if Q.empty():  # ����Ϊ�գ���ʾ�޽�
            return False
        here = Q.get()  # ��һ����չ���
    Pathlen = grid[finish.row, finish.col] - 2
    PathLen1 = Pathlen
    here = finish
    for j in range(Pathlen - 1, -1, -1):  # ����Ѱ��·��
        path.append(Position(here.row, here.col))  # ����ǰ�����·��
        for i in range(NumofNbers):
            nbr.row = here.row + offset[i].row
            nbr.col = here.col + offset[i].col
            if grid[nbr.row, nbr.col] == j + 2:  # �ҵ���һ������
                break
        here = Position(nbr.row, nbr.col)  # ����Ϊ��һ������
    return True

def main():
    global path, PathLen1
    n, m = 7, 7     #  m,n��ʾ���������������
    grid = np.zeros((n + 2, m + 2), dtype=int)   #  ��ʼ������
    #   ���뷽���ֵ
    for i in range(1, n + 1):
        grid[i, 1:n + 1] = np.array(input().split(), dtype=int)

    start_x, start_y = 3, 2        #   ��������
    finish_x, finish_y = 4, 6        #    �յ������
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


