#лучшее nlog^2(n)
#худшее n^2

import math
def sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

array = [23, 91, 558, 55, 13, 213]
print("Исходный массив: ", array)
sort(array)
print("Отсортированный массив: ", array)
