import re
import find_separ


def cisco_find():
    # Открываем файл с конфигом cisco
    file_cisco = open('172.16.0.65.txt', 'r')

    # Запускаем цикл с условием
    # пробегаемся по строчкам конфига и ищем строку с username
    #
    with open('append_new.txt', 'w') as file4:
        for line in file_cisco:
            pattern = re.compile('username')
            match = pattern.search(line)

            # Если находится такая строка удаляем пробел в конце
            # отделяем по разделителю (пробел)
            # и выбираем следующее слово за username
            # дописываем каждое найденное слово в файл
            if match:
                m = match.string.strip()
                parts = m.rsplit(' ')
                res = parts[1]
                print('Пользователи в конфиге:')
                print(res)
                file4.write(res + '\n')

    # Запускаем функцию сравнения файлов
    find_separ.separate()


cisco_find()
