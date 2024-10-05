class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding="utf-8") as file:
                s1 = ""
                for line in file:
                    line1 = line.lower()
                    l = len(line)
                    for j in range(l):
                        if ',.=!?;:'.find(line1[j]) > -1:
                            continue
                        elif j + 1 < l:
                            if line1[j] == " " and line1[j + 1] == "-":
                                j += 2
                                continue
                        s1 = s1 + line1[j]
                all_words[i] = s1.split()
        return all_words

    def find(self, word):
        dict = self.get_all_words()
        s1 = list(dict)
        s3 = {}
        for i in s1:
            s2 = dict[i]
            k = 0
            for j in s2:
                k += 1
                if j == word.lower():
                    s3[i] = k
                    break
        return s3

    def count(self, word):
        dict = self.get_all_words()
        s1 = list(dict)
        s3 = {}
        for i in s1:
            s2 = dict[i]
            k = 0
            for j in s2:
                if j == word.lower():
                    k += 1
            s3[i] = k
        return s3


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
