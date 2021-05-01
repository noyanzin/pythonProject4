'''
Реализовать два небольших скрипта:
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
'''


from itertools import count, cycle


def create_generator(my_list=[]):
    for i in my_list:
        my_list.append(i)
        yield i


my = create_generator([0, 1, 2])
for i in range(10):
    print(next(my))

print('NEXT1')


def iter1(start1: int, stop1: int):
    for i in count(start1):
        if i > stop1:
            break
        else:
            yield i


print('NEXT2')

a = list(iter1(10, 15))
count = 0
for item in cycle(a):
    if count > 30:
        break
    print(item)
    count += 1
