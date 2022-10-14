''' Lab_2. Task 2.
Написати Python-скрипт, який за допомогою p однотипних потоків обчислює
добуток матриць A (m × n) і B (n × k). Результат обчислень вивести
в стандартний потік виведення.
'''

import threading
from time import sleep
import numpy as np


class MatrixCalculationProduct(threading.Thread):
    ''' Calculation the product of matrices A (m × n) and B (n × k) in
    streams of the same type. The result of the calculation is output
    to the standard output stream.
    '''

    def __init__(self, arrayA, arrayB):
        super().__init__()
        self.arrayA = arrayA
        self.arrayB = arrayB

    def run(self):
        ''' Display the calculation result to the standard output stream.'''
        print(f'{self.name} started!')
        print(f'{self.name} result:\n{self.product(self.arrayA, self.arrayB)}')
        sleep(.3)
        print(f'{self.name} finished!')

    def product(self, arrayA, arrayB):
        ''' Calculates the product of matrices.'''
        return np.dot(arrayA, arrayB)


if __name__ == '__main__':
    m = 3
    n = 4
    k = 5
    rg = np.random.default_rng(1)

    for x in range(1, 5):
        arrayA = rg.random((m, n))
        arrayB = rg.random((n, k))

        thread = MatrixCalculationProduct(arrayA, arrayB)
        thread.start()
        sleep(.1)
