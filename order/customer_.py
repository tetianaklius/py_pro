class Customer:
    def __init__(self, name: str, age: str, phone_number: str, city: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.city}, phone number: {self.phone_number}"
