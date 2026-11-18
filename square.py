def area(a):
    """Возвращает площадь квадрата со стороной a.

    Пример:
        area(3)
    """
    if a < 0:
        raise ValueError("Сторона должна быть неотрицательной")
    return a * a


def perimeter(a):
    """Возвращает периметр квадрата со стороной a.

    Пример:
        perimeter(3)
    """
    if a < 0:
        raise ValueError("Сторона должна быть неотрицательной")
    return 4 * a
