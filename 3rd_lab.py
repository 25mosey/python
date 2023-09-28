def find_max_element(numbers):
    if not numbers:
        return None, None
    max_value = numbers[0]
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
    return max_value, max_index
numbers = [3, 7, 2, 8, 5, 9]
max_value, max_index = find_max_element(numbers)
if max_value is not None and max_index is not None:
    print("Наибольший элемент:", max_value)
    print("Индекс наибольшего элемента:", max_index)
else:
    print("Список пустой")
