def podschet(*args):
    # print(args)
    s1 = str(*args)
    l = len(s1)
    i = 0
    s = 0
    while i < l:
        if s1[i].isdigit() == True:
            j = 0
            while i < l and s1[i].isdigit() == True:
                j = j * 10 + int(s1[i])
                i = i + 1
            s = s + j
        elif i < l and s1[i] == "'":
            i = i + 1
            while i < l and s1[i] != "'":
                s = s + 1
                i = i + 1
        elif i < l and s1[i] == '"':
            i = i + 1
            while i < l and s1[i] != '"':
                s = s + 1
                i = i + 1
        i = i + 1
    return s


ss = (input("введите без перевода строк "))
print()
print(podschet(ss))
# [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
