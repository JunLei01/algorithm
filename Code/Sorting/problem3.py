from createRandomNumber import randomInt

def InsertSort(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            j = i
            while j >= 0 and numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                j -= 1
    return numbers

if __name__ == "__main__":
    numbers = []
    for i in range(0, 100000):
        number = randomInt()
        numbers.append(number)
    print("排序前：",numbers)
    numbers = InsertSort(numbers)
    print("排序后：",numbers)


# ###  希尔排序
# from createRandomNumber import randomInt
#
# def ShellSort(numbers):
#     gap = int(len(numbers) / 2)
#     while gap > 0:
#         for i in range(gap, len(numbers)):
#             key = numbers[i]
#             j = i - gap
#             while j >= 0 and numbers[j] > numbers[j+gap]:
#                 numbers[j+gap], numbers[j] = numbers[j], numbers[j+gap]
#                 j -= gap
#         gap = int(gap / 2)
#     return numbers
#
# if __name__ == "__main__":
#     numbers = []
#     for i in range(0, 11):
#         number = randomInt()
#         numbers.append(number)
#     print(numbers)
#     numbers = ShellSort(numbers)
#     print(numbers)
#
#
#
