def make_en():
    first_name = input('Введите имя контакта: ')
    second_name = input('Введите фамилию контакта: ')
    phone = input('Введите телефон контакта: ')
    with open('folder.txt', 'a') as f:
        f.write(f'\n{first_name}, {second_name}, {phone}')
    start_en()
def find_en():
    name = input('Введите имя, фамилию или телефон контакта для поиска: ')
    with open ('folder.txt', 'r') as f:
        for i in f.readlines():
            if name in i:
                print('\n Искомый контакт: ', i, end = ' ')
    start_en()
def rename_en():
    with open('folder.txt', 'r') as f:
        name = input('Введите имя фамилию или телефон контакта, который нужно изменить: ')
        copy = f.readlines()
        for i in copy:
            if name in i:
                q = i
                print(f'Контакт {i} будет удален')
        a = []
        for j in copy:
            if j == q:
                continue
            else:
                a.append(j)

        with open('folder.txt', 'w') as f:
            for k in a:
                f.write(k)

    new_name = input('Введите новое имя контакта: ')
    new_family = input('Введите новую фамилию контакта: ')
    new_phone = input('Введите новый телефон контакта: ')
    with open('folder.txt', 'a') as f:
        f.write(f'\n{new_name}, {new_family}, {new_phone}')
    start_en()

def start_en():
    print('\n Здравствуйте. Я - ваш телефонный справочник')
    print('Для выхода нажмите Enter')
    print('Для дальнейшей работы выберите цифру: ')
    print('''
        1 - добавить новый контакт
        2 - поиск контакта в телефонной книге
        3 - изменить существующий контакт
        ''')
    a = int(input('Введите цифру: '))
    match a:
        case 1:
            make_en()
        case 2:
            find_en()
        case 3:
            rename_en()
###################################################################
def make_rus():
    first_name = input('Введите имя контакта: ')
    second_name = input('Введите фамилию контакта: ')
    phone = input('Введите телефон контакта: ')
    with open('folder.txt', 'a', encoding = 'utf-8') as f:
        f.write(f'\n{first_name}, {second_name}, {phone}')
    start_rus()
def find_rus():
    name = input('Введите имя, фамилию или телефон контакта для поиска: ')
    with open ('folder.txt', 'r', encoding = 'utf-8') as f:
        for i in f.readlines():
            if name in i:
                print('\n Искомый контакт: ', i, end = ' ')
    start_rus()
def rename_rus():
    with open('folder.txt', 'r', encoding = 'utf-8') as f:
        name = input('Введите имя фамилию или телефон контакта, который нужно изменить: ')
        copy = f.readlines()
        for i in copy:
            if name in i:
                q = i
                print(f'Контакт {i} будет удален')
        a = []
        for j in copy:
            if j == q:
                continue
            else:
                a.append(j)

        with open('folder.txt', 'w', encoding = 'utf-8') as f:
            for k in a:
                f.write(k)

    new_name = input('Введите новое имя контакта: ')
    new_family = input('Введите новую фамилию контакта: ')
    new_phone = input('Введите новый телефон контакта: ')
    with open('folder.txt', 'a', encoding = 'utf-8') as f:
        f.write(f'\n{new_name}, {new_family}, {new_phone}')
    start_rus()
    
def start_rus():
    print('\n Здравствуйте. Я - ваш телефонный справочник')
    print('Для выхода нажмите Enter')
    print('Для дальнейшей работы выберите цифру: ')
    print('''
        1 - добавить новый контакт
        2 - поиск контакта в телефонной книге
        3 - изменить существующий контакт
        ''')
    a = int(input('Введите цифру: '))
    match a:
        case 1:
            make_rus()
        case 2:
            find_rus()
        case 3:
            rename_rus()


#################################################################333


def language():
    print('''
        1 - английский язык
        2 - русский язык
        ''')
    q = int(input('выберите язык ввода: '))
    match q:
        case 1:
            start_en()
        case 2:
            start_rus()

    
language() 