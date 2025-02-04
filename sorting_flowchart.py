numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(numbers)


def the_algorithm():
    i = 0
    N = len(numbers)
    while i < (N - 1):
        j = 0
        while j < (N - i - 1):
            while numbers[j] > numbers[j + 1]:
                temp = numbers[j + 1]
                numbers[j + 1] = numbers[j]
                numbers[j] = temp
            else:
                j = j + 1
        else:
            i = i + 1
    else:
        print(numbers)


the_algorithm()
