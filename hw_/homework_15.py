import sys


class Rectangle:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area() + other.area()
        if isinstance(other, int | float):
            return self.area() + other
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.area() * other
        return NotImplemented

    def __str__(self):
        return f"{self.x} x {self.y}"


ra_1 = Rectangle(2, 4)
ra_2 = Rectangle(3, 5)
ra_3 = Rectangle(30, 0.5)


print(ra_1 < ra_2)
print(ra_1 < ra_3)
print(ra_2 < ra_3)
print(ra_2 == ra_3)
print(ra_2 > ra_1)

print(ra_1 + ra_2)
print(ra_1 + ra_3)

print(ra_1 * 3)
print(ra_3 * 0.5)
print(ra_3 * 10)


import math


class Rational:
    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError("A must be int")
        if not isinstance(b, int):
            raise TypeError("B must be int")
        if not b:
            raise ZeroDivisionError()
        self.__a = a
        self.__b = b

    def __eq__(self, other):
        k = math.gcd(self.__a, self.__b)
        self.__a //= k
        self.__b //= k

        k = math.gcd(other.__a, other.__b)
        other.__a //= k
        other.__b //= k
        return (self.__a, self.__b) == (other.__a, other.__b)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__a / self.__b < other.__a / other.__b

    def __gt__(self, other):
        return self.__a / self.__b > other.__a / other.__b

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        b = self.__b * other.__b
        a = b // self.__b * self.__a - \
            b // other.__b * other.__a
        return Rational(a, b)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)

        b = self.__b * other.__b
        a = b // self.__b * self.__a - \
            b // other.__b * other.__a
        return Rational(a, b)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        sign = 1 if self.__a * self.__b > 0 else -1

        b = abs(self.__b) * abs(other.__b)
        a = b // abs(self.__b) * abs(self.__a) \
            - b // abs(other.__b) * abs(other.__a)
        self.__a = sign * a
        self.__b = b
        return self

    def __str__(self):
        sign = "" if self.__a * self.__b > 0 else "-"
        a, b = abs(self.__a), abs(self.__b)
        k = math.gcd(a, b)
        a //= k
        b //= k

        if a == b:
            return f"{sign}1"
        if b == 1:
            return f"{sign}{a}"
        if a > b:
            return f"{sign}{a // b} {a - a // b * b}/{b}"

        return f"{sign}{a}/{b}"





r_1 = Rational(4, 5)
r_2 = Rational(3, 8)
r_3 = Rational(8, 10)
r_4 = Rational(1, 8)
r_5 = Rational(3, 8)
r_1 -= r_2
print(r_4 - 2 - r_2)
print(r_1)
print(r_2 > r_3)
print(r_4 < r_2)
print(r_4 == r_2)
print(r_2 == r_5)

