def all_variants(text):
    l = len(text)
    a = 0
    i = 0
    while i <= l:
        yield text[a:a + i]
        if a + i < l:
            a = a + 1
        else:
            a = 0
            i += 1


a = all_variants("abc")
for i in a:
    print(i)
