# 1. Add the Group class (hw2) with the ability to support an iterative protocol.

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    surname: str
    age: str


class Group:
    def __init__(self, title, max_students=10):
        self.title = title
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if student not in self.students and len(self.students) < self.max_students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_student(self, surname):
        res = []
        for student in self.students:
            if student.surname == surname:
                res.append(student)
        return res

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.students[item]
        raise TypeError

    def __iter__(self):
        return GroupIter(self.students)

    def __str__(self):
        return "\n".join(map(str, self.students))


class GroupIter:
    def __init__(self, students):
        self.items = items
        self.index = 0

    def __next__(self):
        if self.index < len(self.items):
            self.index += 1
            return self.items[self.index - 1]
        raise StopIteration


student_1 = Student("Hanna", "Shepit", "35")
student_2 = Student("Serhii", "Haiduk", "22")
student_3 = Student("Andrii", "Melnyk", "19")
student_4 = Student("Oksana", "Dovzhenko", "20")
student_5 = Student("Marta", "Buriak", "23")
student_6 = Student("Lida", "Vasylenko", "25")
student_7 = Student("Yurii", "Kozak", "26")
student_8 = Student("Olha", "Nesterenko", "32")
student_9 = Student("Denys", "Zhuk", "29")
student_10 = Student("Ostap", "Stelmakh", "18")

group = Group("Python")
group.add_student(student_1)
group.add_student(student_2)
group.add_student(student_3)
group.add_student(student_4)
group.add_student(student_5)

print(group[3])
print(group)

# 2. Modify the Order class (hw1) by adding the implementation of the sequence protocol and the iteration protocol.


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.quantities = []
        self.prices = []

    def add_product(self, product, price, quantity=1):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
            self.prices.append(price)
        else:
            self.products.append(product)
            self.quantities.append(quantity)
            self.prices.append(price)

    def total_cost(self):
        suma = 0
        for index, item in enumerate(self.products):
            suma += item.price * self.quantities[index]
        return suma

    def __iter__(self):
        return OrderIter(self.products, self.prices, self.quantities)

    def __str__(self):
        res = '\n'.join(map
                (lambda item: f"{item[0]} × {item[1]} = {item[0].price * item[1]} UAH",
                zip(self.products, self.quantities))
                )
        return f"{customer}\n-order-\n{res}\nTotal: {self.total_cost()} UAH"

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.products[item]
        raise TypeError


class OrderIter:
    def __init__(self, products, prices, quantities):
        self.products = products
        self.prices = prices
        self.quantities = quantities
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1], self.prices[self.index - 1], self.quantities[self.index - 1]
        raise StopIteration


class Customer:
    def __init__(self, name: str, age: str, phone_number: str, city: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.city}, phone number: {self.phone_number}"


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"


milk = Product("milk", 25)
grapefruit = Product("grapefruit", 75)
chocolate = Product("chocolate", 45)
pineapple = Product("pineapple", 95)

customer = Customer("Andrii", "35", "380_66_451_5878", "Lviv")
order = Order(customer)
order.add_product(milk, 25, 1)
order.add_product(grapefruit, 75, 3)
order.add_product(chocolate, 45, 2)
order.add_product(pineapple, 95, 1)


print(order[2])
print(iter(order))
for item in order:
    print(item)

for product, price, quantity in order:
    print(product.name, price * quantity)

print()

x = iter(order)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

