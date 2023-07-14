import os


def print_info(temp):
    temp = [w.replace(';', ' ') for w in temp]
    print(* temp, sep='\n')


def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as file:
        temp = [i.strip() for i in file]
        return temp


def write_file(data):
    temp = [i.replace(' ', ';') for i in data]
    with open('my_file.txt', 'w') as file:
        for i in temp:
            file.write(i + '\n')


def appends(data):
    temp = list(input('Введите ФИО и номер: ').split(';'))
    data += temp
    write_file(data)
    return menu()


def contact_search(data):
    data = [w.replace(';', ' ') for w in data]
    contact = input('Введите контакт: ')
    print("=" * 35)
    for i, line in enumerate(data):
        if contact in line: print(i, line)
        
        
def phonebook_change(data):
    contact_search(data)
    temp = [w.replace(';', ' ') for w in data]
    number = int(input('Введите № контакта для изменение: '))
    modifie_contract = input('Введите ФИО и номер: ')
    temp [number] = modifie_contract
    write_file(temp)
    return menu()


def phonebook_del(data):
    contact_search(data)
    temp = [w.replace(';', ' ') for w in data]
    number = int(input('Введите № контакта для удаления: '))
    del temp[number]
    write_file(temp)
    return menu()


def close(data):
    return write_file(data)


def menu():
    data = read_file()
    while True:
        print('§' * 40)
        print('Выберите действие: ')
        print('1 - вывести инфо на экран')
        print('2 - добавить контакт')
        print('3 - поиск контакта')
        print('4 - изменить контакт')
        print('5 - удалить контакт')
        print('0 - выход из программы')
        n = int(input('ваш выбор: '))
        clear = lambda: os.system('clear')
        clear()
        if n == 0:
            return close(data)
        elif n == 1:
            print_info(data)
        elif n == 2:
            return appends(data)
        elif n == 3:
            contact_search(data)
        elif n == 4:
            return phonebook_change(data)
        elif n == 5:
            return phonebook_del(data)


if __name__ == '__main__':
    menu()
