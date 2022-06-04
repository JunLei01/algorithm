import math
from createRandomNumber import randomInt

def heapify(tree, n, parent):
    left = 2 * parent + 1
    right = 2 * parent + 2
    min = parent
    if left < n and tree[left] < tree[min]:
        min = left
    if right < n and tree[right] < tree[min]:
        min = right
    if min != parent:
        tree[min], tree[parent] = tree[parent], tree[min]
        heapify(tree, n, min)

def build_heap(tree):
    last_node = len(tree) - 1
    for i in range(last_node, -1, -1):   # 从最后一个节点开始构建树
        heapify(tree, len(tree), i)

def heap_sort(tree):
    build_heap(tree)
    length = len(tree)
    for i in range(length-1, 0, -1):
        tree[i], tree[0] = tree[0], tree[i]
        heapify(tree, i, 0)


if __name__ == "__main__":
    numbers = []
    for i in range(0, 100000):
        number = randomInt()
        numbers.append(number)
    print("排序前：",numbers)
    heap_sort(numbers)
    print("排序后：", numbers)
