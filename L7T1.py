# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random

size = 20
arr = [random.randint(-100, 100) for _ in range(size)]
print(arr)

counter = len(arr)

while counter:
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    counter -= 1
print(arr)
