''' Lab_2. Task 3.
Написати Python-скрипт, який виконує багатопотокову обробку текстових файлів
в заданій директорії. Текстові файли в директорії названі таким чином:
in_i.txt, де i - натуральне число. Кожен файл складається з двох рядків:
перший рядок - бінарний оператор ("+", "-", "*", "/"), другий - дійсні числа,
розділені пробілом. Python-скрипт повинен виконати зазначені дії
над числами в кожному файлі і суму результатів записати в файл out.txt.
'''

import threading
from pathlib import Path
from os import scandir


class writingCalculationsToFiles(threading.Thread):
    def __init__(self, path, file):
        super().__init__()
        self.path = path
        self.file = file

    def run(self):
        path_to_file = f'{self.path}in{Path().resolve().root}{self.file}'
        with open(path_to_file) as file_read:
            lines = file_read.readlines()
            operator = lines[0][0]
            numbers = lines[1].split(' ')
            result = operator.join([numbers[0], numbers[1]])

            with open(f'{self.path}out.txt', 'a') as file_write:
                file_write.write(f'{result} = {eval(result)}\n')


if __name__ == '__main__':
    absolute_path = Path().resolve()
    relative_path = f'{absolute_path}{absolute_path.root}'

    with open(f'{relative_path}out.txt', 'w') as file_write:
        file_write.flush()

    for file in scandir(path=f'{relative_path}in'):
        writingCalculationsToFiles(relative_path, file.name).start()
