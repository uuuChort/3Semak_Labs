# Постоянное время n^2

def sort(array):
    for num in range(len(array)):
        min_value = num
        for item in range(num, len(array)):
            if array[min_value] > array[item]:
                min_value = item
        array[num], array[min_value] = array[min_value], array[num]
    return (array)

array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
sort(array)
print("Отсортированный массив: ", array)
