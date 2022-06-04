from createRandomNumber import randomInt
def quick_sort(numbers, i, j):
    if i >= j:
        return numbers
    flag = numbers[i]
    low = i
    high = j
    while i < j:
        while i < j and numbers[j] >= flag:
            j -= 1
        numbers[i] = numbers[j]
        while i < j and numbers[i] <= flag:
            i += 1
        numbers[j] = numbers[i]
    numbers[j] = flag
    quick_sort(numbers, low, i-1)
    quick_sort(numbers, i+1, high)
    return numbers
if __name__ == "__main__":
    numbers = []
    for i in range(0, 100000):
        number = randomInt()
        numbers.append(number)
    print("排序前：",numbers)
    numbers = quick_sort(numbers, 0, len(numbers)-1)
    print("排序后：",numbers)
