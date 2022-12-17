import person_


class Student(person_.Person):
    def __init__(self, name: str, surname: str, age: int):
        if not isinstance(age, int):
            raise TypeError()
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f"{super().__str__()}, {self.age} y.o."