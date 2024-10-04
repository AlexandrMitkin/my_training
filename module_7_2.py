from idlelib.iomenu import encoding


def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding="utf-8")
    strings_positions = {}
    k1 = 0
    for i in strings:
        k1 += 1
        k2 = f.tell()
        f.write(i + "\n")
        strings_positions[(k1, k2)] = i
    f.close()
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
