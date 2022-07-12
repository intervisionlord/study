from math import sqrt


def triangle_perimeter(lenA: float,
                       lenB: float,
                       lenC: float):
    """Вычисление периметра треугольника по 3м сторонам

    Args:
        lenA (float): Длина стороны A
        lenB (float): Длина стороны B
        lenC (float): Длина стороны C
    """
    return sum([lenA, lenB, lenC])
    
def triangle_area(lenA: float,
                  lenB: float,
                  lenC: float):
    """Вычисление площади треугольника по формуле Герона

    Args:
        lenA (float): Длина стороны A
        lenB (float): Длина стороны B
        lenC (float): Длина стороны C
    """
    halfPerim = sum([lenA, lenB, lenC]) / 2
    triangArea = sqrt(halfPerim * (halfPerim - lenA) * (halfPerim - lenB) * (halfPerim - lenC))
    return triangArea
    
if __name__ == '__main__':
    lenA, lenB, lenC = input('Введите стороны трегольника (через пробел): ').split()
    print('Периметр треугольника:',
          triangle_perimeter(float(lenA),
                             float(lenB),
                             float(lenC)))
    print('Площадь треугольника:',
          triangle_area(float(lenA),
                        float(lenB),
                        float(lenC)))