from createRandomNumber import randomInt

def SelectionSort(numbers):
    for i in range(len(numbers)):
        minIndex = i
        for j in range(i, len(numbers)):
            if numbers[minIndex] > numbers[j]:
                minIndex = j
        numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
    return numbers

if __name__ == "__main__":
    numbers = []
    for i in range(0, 100000):
        number = randomInt()
        numbers.append(number)
    print("排序前：",numbers)
    numbers = SelectionSort(numbers)
    print("排序后：", numbers)
