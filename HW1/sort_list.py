def sort_list_imperative(numbers: list[int]) -> None:
    for i in range(0, len(numbers) - 1):
        max_position = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_position]:
                max_position = j
        if (i != max_position):        
            numbers[i], numbers[max_position] = numbers[max_position], numbers[i]

def sort_list_declarative(numbers: list[int]) -> None:
    numbers.sort(reverse=True)


numbers = [1, 9, 4, 0, 7, 2, 6, 3, 8, 2]
numbers1, numbers2 = numbers, numbers
sort_list_imperative(numbers1)
sort_list_declarative(numbers2) 
print("Imperative sorted:\n", numbers1)
print("Declarative sorted:\n", numbers2)
