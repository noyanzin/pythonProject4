'''
Урок 4.Задание 2.
    Представлен список чисел.
    Необходимо вывести элементы исходного списка,
    значения которых больше предыдущего элемента.
'''
import sys
import random as rand

l = [rand.randrange(1, 100, 1) for i in range(20)]
l_out = []
b = sys.maxsize
for a in l:
    if a > b:
        l_out.append(a)
    b = a

print(f'Входная последовательность: {l}')
print(f'Выходная последовательность: {l_out}')
