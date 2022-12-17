# 1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
# опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"


hiking_backpack_1 = Product("Aurora", 5155)
hiking_backpack_2 = Product("Yellow", 4135)
hiking_backpack_3 = Product("Highland", 7867)
print(hiking_backpack_3)
print(hiking_backpack_1.name)


# Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище, ім'я, по батькові,
# мобільний телефон тощо.

class Customer:
    def __init__(self, name: str, age: str, phone_number: str, city: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.city}, phone number: {self.phone_number}"


customer_1 = Customer("Olha", "28", "380_77_672_7777", "Kyiv")
customer_2 = Customer("Andrii", "35", "380_66_451_5878", "Lviv")
customer_3 = Customer("Marta", "42", "380_55_234_6789", "Dnipro")



# Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: float =1):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total_cost(self):
        suma = 0
        for index, item in enumerate(self.products):
            suma += item.price * self.quantities[index]
        return suma

    def __str__(self):
        res = '\n'.join(map
                (lambda item: f"{item[0]} × {item[1]} = {item[0].price * item[1]} UAH",
                zip(self.products, self.quantities))
                )
        return f"{customer}\n-order-\n{res}\nTotal: {self.total_cost()} UAH"


milk = Product("milk", 25)
grapefruit = Product("grapefruit", 75)
chocolate = Product("chocolate", 45)

customer = Customer("Andrii", "35", "380_66_451_5878", "Lviv")

order = Order(customer)

order.add_product(milk, 1)
order.add_product(grapefruit, 3)
order.add_product(chocolate, 2)

print(order)
