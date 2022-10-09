'''Lab_2. Task 2
Написати Python-скрипт, який за допомогою p однотипних потоків обчислює
добуток матриць A (m × n) і B (n × k). Результат обчислень вивести
в стандартний потік виведення.
'''

import threading
from time import sleep
import numpy as np


class MyThread(threading.Thread):

    def __init__(self, arrayA, arrayB):
        super().__init__()
        self.arrayA = arrayA
        self.arrayB = arrayB

    def run(self):
        print(f'{self.name} started!')
        print(f'{self.name} result:\n{self.product(self.arrayA, self.arrayB)}')
        sleep(.3)
        print(f'{self.name} finished!')

    def product(self, arrayA, arrayB):
        return np.dot(arrayA, arrayB)


if __name__ == '__main__':
    m = 3
    n = 4
    k = 5
    rg = np.random.default_rng(1)

    for x in range(1, 5):
        arrayA = rg.random((m, n))
        arrayB = rg.random((n, k))

        mythread = MyThread(arrayA, arrayB)
        mythread.start()
        sleep(.1)
