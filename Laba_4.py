# Сортировка прочесыванием.

# Худшее n^2
# Лучшее nlogn


def sort(array):
    step = int(len(array)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(array):
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)
array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
sort(array)
print("Отсортированный массив:", array)
