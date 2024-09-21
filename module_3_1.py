calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    l = len(string)
    str1 = string.upper()
    str2 = string.lower()
    count_calls()
    return (l, str1, str2)


def is_contains(string, list_to_search):
    # if list_to_search.count(string.upper()) > 0:
    count_calls()
    for i in list_to_search:
        if str(i).upper() == string.upper():
            return True
    return False


def vibor():
    while 1 > 0:
        print("нажмите Enter или введите одну или несколько строк через запятую ")
        s = input()
        if s == "":
            break
        else:
            s1 = ""
            s2 = []
            s3 = ""
            r = 1
            for i in s:
                if r == 2 and i != ",":
                    s3 = s3 + i
                elif r == 2 and i == ",":
                    s2.append(s3)
                    s3 = ""
                elif r == 1 and i != ",":
                    s1 = s1 + i
                elif r == 1 and i == ",":
                    r = 2
            if r == 1:
                print(string_info(s1))
            else:
                s2.append(s3)
                print("s1= ", s1, " s2= ", s2)
                print(is_contains(s1, s2))


vibor()
print(calls)
