import math


def area(r):
    """Возвращает площадь круга с радиусом r.

    Пример:
        area(3)
    """
    return math.pi * r * r


def perimeter(r):
    """Возвращает длину окружности с радиусом r.

    Пример:
        perimeter(3)
    """
    return 2 * math.pi * r