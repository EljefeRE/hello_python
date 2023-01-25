def get_op():
    op = int(input(
        '1 - добавить пользователя \n2 - вывести таблицу контактов \n3 - вывести только имя и фамилью \n4 - отсортировать по именам \n5 - отсортировать по id \n6 - выход \n'))
    return op

def add_user():
    id = input('Введите id: ')
    name = input('Введите Имя: ')
    lastname = input('Введите Фамилию: ')
    number = input('Введите номер телефона: ')
    comments = input('Введите комментарий: ')
    line = f'{id},{name},{lastname},{number},{comments}\n'
    with open('user_list.txt', 'a') as file:
        file.write(line)
    print('Сохранено!')

def print_table():
    with open('user_list.txt', 'r') as file:
        for line in file.readlines():
            print(line, end='')

def print_only_names():
    with open('user_list.txt', 'r') as file:
        lst = file.readlines()
        for line in lst:
            a = line.strip().split(',')
            print(f'Имя - {a[1]}, Фамилия - {a[2]}')