def read_file_into_dict(filename):
    """
    Функция для чтения файла и превращения его данных в словарь.
    :param filename: имя файла
    :return: словарь с данными из файла
    """

    # Открываем файл
    with open(filename, 'r') as file:
        # Создаём пустой словарь
        data_dict = {}

        # Проходимся по каждой строке в файле
        for line in file:
            # Разделяем строку на ключ и значение
            key, value = line.strip().split('\n')

            # Добавляем пару ключ-значение в словарь
            data_dict[key] = value

    return data_dict

# Пример использования функции
filename = 'example.txt'  # Замените на имя вашего файла
data_dict = read_file_into_dict(filename)

# Выводим словарь
print(data_dict)