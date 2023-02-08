list_sequence_nums = [int(item) for item in input("Введите последовательность чисел через пробел: ").split()]
user_num = int(input("Введите любое число: "))

# Сортировка
def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# Определение позиции элемента
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "Число выходит за диапазон списка, введите меньше число. "

print(f"Последовательность списка по возрастанию: {list_sequence_nums}")


if not binary_search(list_sequence_nums, user_num, 0, len(list_sequence_nums)):
    elem = min(list_sequence_nums, key=lambda x: (abs(x - user_num), x))
    ind = list_sequence_nums.index(elem)
    max_ind = ind + 1
    min_ind = ind - 1
    if elem < user_num:
        print(f"В списке нет введенного элемента. \nБлижайщий меньший элемент: {elem}, его индекс: {ind} \nБлижайщий большой элемент: {list_sequence_nums[max_ind]} его индекс: {max_ind}")
    elif min_ind < 0:
        print(f"В списке нет введенного эдемента. \nБлижайщий больший элемент: {elem}, его индекс: {list_sequence_nums.index(elem)}. \nВ списке нет меньшего элемента ")
    elif elem > user_num:
        print(f"В списке нет введенного элемента. \nБлижайший больший элемент: {elem}, его индекс: {list_sequence_nums.index(elem)} \nБлижайший меньший элемент: {list_sequence_nums[min_ind]}, его индекc: {min_ind}")
    elif list_sequence_nums.index(elem) == 0:
        print(f"Индекс введенного элемента: {list_sequence_nums.index(elem)}")
else:
    print(f"Индекс введенного элемента: {binary_search(list_sequence_nums, user_num, 0, len(list_sequence_nums))}")