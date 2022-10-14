''' Lab_2. Task 1.
Написати Python-скрипт, який створює чотири потоки. Кожен потік повинен
викликати функцію, яка виводить в стандартний потік виведення
послідовність рядків, переданих у функцію у вигляді аргументу.
'''

import threading
import time


class DemonstrationThread(threading.Thread):
    ''' Outputs to the standard output stream the sequence of strings passed to
    the function as an argument.
    '''

    def run(self):
        print(f'{self.name} started!')
        time.sleep(.3)
        print(f'{self.name} finished!')


if __name__ == '__main__':
    for x in range(1, 5):
        thread = DemonstrationThread(name=f'Thread-{x}')
        thread.start()
        time.sleep(.1)
