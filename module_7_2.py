from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')                      # кодировка
    number_str = 1                                                     # записываемая строка
    for i in strings:
        byte_position = file.tell()                                    #  получения номера байта
        strings_positions[(number_str, byte_position)] = i             #  словарь (<номер строки>, <байт начала строки>)
        file.write(i + '\n')                                           #  запись
        number_str += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)