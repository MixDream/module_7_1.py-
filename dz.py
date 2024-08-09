class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.category == other.category

    def to_string(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        try:
            with open(self.__file_name, 'r') as f:
                self.products = [Product(*line.strip().split(', ')) for line in f.readlines()]
        except FileNotFoundError:
            self.products = []

    def save_products(self):
        with open(self.__file_name, 'w') as f:
            for product in self.products:
                f.write(product.to_string() + '\n')

    def add(self, *products):
        for product in products:
            if product not in self.products:
                self.products.append(product)
            else:
                print(f"Продукт {product.name} уже есть в магазине")

        self.save_products()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

for product in s1.products:
    print(product)
