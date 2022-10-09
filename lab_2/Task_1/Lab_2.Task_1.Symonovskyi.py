'''Lab_2. Task 1
Написати Python-скрипт, який створює чотири потоки. Кожен потік повинен
викликати функцію, яка виводить в стандартний потік виведення
послідовність рядків, переданих у функцію у вигляді аргументу.
'''

import threading
import time


class MyThread(threading.Thread):

    def run(self):
        print(f'{self.name} started!')
        time.sleep(.3)
        print(f'{self.name} finished!')


if __name__ == '__main__':
    for x in range(1, 5):
        mythread = MyThread(name=f'Thread-{x}')
        mythread.start()
        time.sleep(.1)
