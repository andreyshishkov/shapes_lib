from .shape import Shape
from math import sqrt
from .exception import WrongSidesTriangleException


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if not self.__is_valid_triangle(a, b, c):
            raise WrongSidesTriangleException
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_valid_triangle(a: float, b: float, c: float) -> bool:
        if a >= (b + c) or b >= (a + c) or c >= (a + b):
            return False
        return True

    def get_square(self) -> float:
        p = (self.a + self.b + self.c) / 2
        square = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return square

    def is_right_triangle(self):
        return self.c ** 2 == self.a ** 2 + self.b ** 2
