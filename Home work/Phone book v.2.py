from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LastNameError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LineNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Не валидное имя')
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input('Введите фамилию: ')
            if len(last_name) < 2:
                raise LastNameError('Не валидное имя')
            else:
                is_valid_last_name = True
        except LastNameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print('Не валидный номер!')
            continue
        except LenNumberError as err:
            print(err)
            continue

    is_valid_line_number = False
    while not is_valid_line_number:
        try:
            line_number = int(input('Введите номер строки для копирования: '))
            if line_number < 1 or line_number > len(line_number):
                raise LineNumberError('Некорректный номер строки')
            else:
                is_valid_line_number = True
        except LineNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number, line_number]


# with это менеджер контекста, используя его нам не надо вызывать close
def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(lst[2]):
            print('Такой телефон уже существует')
            return
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8',
              newline='') as data:  # перезаписываем наш файл; newline = '' - не будет лишних строк
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def copy_line(file_name, file_name2, lines):
    lines = []
    with open(file_name, 'r', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        for row in f_reader:
            lines.append(row)
    with open(file_name2, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data)
        for i in range(int(len(lines))):
            f_writer.writerows(lines[i])
            # if el != line_number - 1:
            #     data.writer(lines[el])
    print('Копирование строки успешно выполнено')
    # f_writer = DictWriter(data, fieldnames = ['Имя', 'Фамилия', 'Телефон'])
    # f_writer.writeheader()
    # return list(f_reader)


# def copy_line2(file_name2, lines):


# data.writer(lines[line_number - 1])


file_name = 'phone.csv'
file_name2 = 'phone2.csv'


def main():
    while True:
        command = input('Введите комманду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует. Создайте его')
                continue
        elif command == 'c':
            if not exists(file_name2):
                create_file(file_name2)
                write_file(file_name2, get_info())
            print(*read_file(file_name))


main()
# copy_line(file_name, file_name2, line_number)