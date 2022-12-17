# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).

class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


person_1 = Person("Hanna", "Shepit")
print(person_1)


# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).

class Student(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f"{super().__str__()}, {self.age} y.o."


person_1 = Student("Hanna", "Shepit", "35")
print(person_1)


# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент. Реалізуйте методи додавання,
# видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.


class Group:
    def __init__(self, title, max_group=10):
        self.title = title
        self.group = []
        self.max_group = max_group

    def add_student(self, student):
        if student not in self.group and len(self.group) < self.max_group:
            self.group.append(student)

    def remove_student(self, student):
        if student in self.group:
            self.group.remove(student)

    def find_student(self, surname):
        res = []
        for student in self.group:
            if student.surname == surname:
                res.append(student)
        return res

    def __str__(self):
        return f"{self.title}:\n" + '; '.join(map(str, self.group))


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

group = Group("group")
group.add_student(student_1)
group.add_student(student_2)
group.add_student(student_3)
group.add_student(student_6)
group.add_student(student_8)
group.add_student(student_9)
group.remove_student(student_9)


res_find = group.find_student("Nesterenko")
for item in res_find:
    print(item)
for item in res_find:
    print(item.name, item.surname, item.age, sep="_")
print(group.find_student("Buriak"))
print(group)
