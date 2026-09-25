class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, int):
            raise TypeError('Price must be an integer')
        elif new_price <= 0:
            raise ValueError('Price must be positive')
        self._price = new_price
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, new_stock):
        if not isinstance(new_stock, int):
            raise TypeError('Stock must be an integer')
        elif new_stock < 0:
            raise ValueError('Stock must be non-negative')
        self._stock = new_stock
    def __len__(self):
        return self._stock
    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError('Product must be an instance of Product')
        result = self.price * self.stock + other.price * other.stock
        return result
    def __repr__(self):
        return (f"Product(name={self.name!r}, "
                f"price={self.price!r}, "
                f"stock={self.stock!r})")
    def __sub__(self, other):
        if not isinstance(other, Product):
            raise TypeError('Product must be an instance of Product')
        result = self.price * self.stock - other.price * other.stock
        return result
    def __eq__(self, other):
        if not isinstance(other, Product):
            raise TypeError('Product must be an instance of Product')
        return self.price == other.price and self.stock == other.stock and self.name == other.name
    def __lt__(self, other):
        return self.price * self.stock < other.price * other.stock
class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, product,quantity):
        if not isinstance(product, Product):
            raise TypeError('Product must be an instance of Product')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer')
        elif quantity <= 0:
            raise ValueError('Quantity must be positive')
        if product.stock < quantity:
            raise ValueError('Quantity must be greater than 0')
        for _ in range(quantity):
            self.items.append(product)
        product.stock -= quantity
    def remove_product(self, product,quantity):
        if not isinstance(product, Product):
            raise TypeError('Product must be an instance of Product')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be an integer')
        elif quantity <= 0:
            raise ValueError('Quantity must be positive')
        if self.items.count(product) < quantity:
            raise ValueError('Quantity must be greater than 0')
        for _ in range(quantity):
            self.items.remove(product)
        product.stock += quantity
    def __len__(self):
        return len(self.items)
    def __contains__(self, product):
        if not isinstance(product, Product):
            raise TypeError('Product must be an instance of Product')
        return product in self.items
    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price
    def __iter__(self):
        return iter(self.items)
    def __getitem__(self,index):
        return self.items[index]
    def __add__(self, other):
        new_cart = Cart()
        new_cart.items.extend(self.items)
        new_cart.items.extend(other.items)
        return new_cart
    def __setitem__(self, index, product):
        if not isinstance(product, Product):
            raise TypeError('Product must be an instance of Product')
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        elif index < 0:
            raise ValueError('Index must be non-negative')
        self.items[index] = product


