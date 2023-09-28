def binary_search (array: list[int], number: int) -> int:
    array.sort()
    left, right = 0, len(array) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] == number:
            return middle
        elif array[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return None

array_test = [54, 12, 0, 84, 45, 37, 5]
find_number_1 = 45
find_number_2 = 107

print("array: ", array_test)
print("index of value {} is {}".format(find_number_1, binary_search(array_test, find_number_1)))
print("index of value {} is {}".format(find_number_2, binary_search(array_test, find_number_2)))


