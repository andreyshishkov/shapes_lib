from shapes.circle import Circle


def test_get_square():
    circle = Circle(radius=5)
    assert round(circle.get_square(), 6) == 78.539816
