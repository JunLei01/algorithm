from createRandomNumber import randomInt

def BubbleSort(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

if __name__ == "__main__":
    numbers = []
    for i in range(0, 10):
        number = randomInt()
        numbers.append(number)
    print("排序前：", numbers)
    numbers = BubbleSort(numbers)
    print("排序后：",numbers)
