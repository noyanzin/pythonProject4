'''
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
'''
from itertools import count, cycle


class InfiniteSum:
    def __init__(self, initial_number):
        self.number_to_square = initial_number

    def __next__(self):
        self.number_to_square = self.number_to_square + 1
        return self.number_to_square

    def __iter__(self):
        return self


c = InfiniteSum(3)
print(next(c))
print(next(c))
print()
