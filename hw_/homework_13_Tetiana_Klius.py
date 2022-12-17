import logging

class Product:
    def __init__(self, name: str, price: float):
        if price <= 0:
            raise ValueError("The price can`t be zero or a negative number")
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} UAH"


milk = Product("milk", 25)
grapefruit = Product("grapefruit", 75.25)
chocolate = Product("chocolate", 45)

print(grapefruit)


class Customer:
    def __init__(self, name: str, age: str, phone_number: str, city: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.city}, phone number: {self.phone_number}"


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
        return f"{self.customer}\n-order-\n{res}\nTotal: {self.total_cost()} UAH"


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name: str, surname: str, age: int):
        if not isinstance(age, int):
            raise TypeError()
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f"{super().__str__()}, {self.age} y.o."


class Group:
    def __init__(self, title: str, max_group):
        if not isinstance(max_group, int):
            raise TypeError()
        if max_group <= 0:
            raise ValueError()
        self.title = title
        self.group = []
        self.max_group = max_group

    def add_student(self, student: Student):
        """

        :param student:
        :return:
        """
        if student in self.group:
            raise DublicateStudentError(student, self.title)
        if len(self.group) >= self.max_group:
            raise GroupLimitError(self.max_group)
        self.group.append(student)
        logger.info("Add student " + str(student.surname))

    def remove_student(self, student: Student):
        """

        :param student:
        :return:
        """
        if student in self.group:
            self.group.remove(student)

    def find_student(self, surname: str):
        """

        :param surname:
        :return:
        """
        res = []
        for student in self.group:
            if student.surname == surname:
                res.append(student)
        return res

    def __str__(self):
        return f"{self.title}:\n" + '\n'.join(map(str, self.group))


class GroupLimitError(Exception):
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __str__(self):
        return f"In this group we already have {self.max_limit} students."


class DublicateStudentError(Exception):
    def __init__(self, student, group_title):
        self.student = student
        self.group_title = group_title

    def __str__(self):
        return f"Student {self.student} registered in {self.group_title}."


logger = logging.getLogger("homework_11_Tetiana_Klius")
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler("../logger.log")
filehandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

logger.info("Started logging")

try:
    group = Group("group", max_group=10)
    group.add_student(Student("Lida", "Vasylenko", 25))   # 1
    group.add_student(Student("Oksana", "Dovzhenko", 20))   # 2
    group.add_student(Student("Yurii", "Kozak", 26))   # 3
    group.add_student(Student("Denys", "Zhuk", 29))   # 4
    group.add_student(Student("Olha", "Nesterenko", 32))   # 5
    group.add_student(Student("Ostap", "Stelmakh", 18))   # 6
    group.add_student(Student("Marta", "Buriak", 23))   # 7
    group.add_student(Student("Hanna", "Shepit", 35))   # 8
    group.add_student(Student("Serhii", "Haiduk", 22))   # 9
    group.add_student(Student("Andrii", "Melnyk", 19))   # 10
    group.add_student(Student("Ivan", "Horyn", 21))

    print(group)

except Exception as error:
    print(error)


logger.info("Finished logging")



