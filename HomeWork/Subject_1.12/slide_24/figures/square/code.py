def square_perimeter(lenA: float):
    """Вычисление периметра квадрата

    Args:
        lenA (float): Сторона квадрата
    """
    return lenA * 4

def square_area(lenA: float):
    """Вычисление площади квадрата

    Args:
        lenA (float): Сторона квадрата
    """
    return lenA ** 2

if __name__ == '__main__':
    lenA = float(input('Введите сторону квадрата: '))
    print('Периметр квадрата:', square_perimeter(lenA))
    print('Площадь квадрата:', square_area(lenA))