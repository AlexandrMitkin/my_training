class Product:
    def __init__(self, name='Potato', weight=50.0, category='Vagetables'):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(Product):
        return Product.name + ", " + str(Product.weight) + ", " + Product.category


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def clear(self):
        f = open(self.__file_name, 'w')
        f.seek(0)
        f.close()

    def get_products(self):
        file = open(self.__file_name, "rt")
        s = file.read()
        file.close()
        return s

    def add(self, *products):
        file = open(self.__file_name, "r")
        s = file.read()
        file.close()
        file = open(self.__file_name, "a+")
        for i in products:
            r = 0
            k = ""
            if isinstance(i, Product):
                k = str(i)
                if s.find(k) > -1:
                    r = 1
                    print(f'Продукт {k} уже есть в магазине')
                    continue
            if r == 0:
                file.write(k)
                file.write("\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print()
print(s1.get_products())
