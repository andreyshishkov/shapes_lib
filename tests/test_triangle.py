from shapes.triangle import Triangle
from shapes.exception import WrongSidesTriangleException
import pytest


def test_triangle__wrong():
    with pytest.raises(WrongSidesTriangleException):
        Triangle(9, 2, 1)

def test_get_square():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_square() == 6

def test_is_right_triangle__right():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_triangle()

def test_is_right_triangle__wrong():
    triangle = Triangle(3, 4, 6)
    assert not triangle.is_right_triangle()

