def is_triangle(sides):
    (a,b,c) = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    (a,b,c) = sides
    if not is_triangle(sides):
        return False
    return a == b == c


def isosceles(sides):
    (a,b,c) = sides
    if not is_triangle(sides):
        return False
    return a == b or b == c or a == c


def scalene(sides):
    (a,b,c) = sides
    if not is_triangle(sides):
        return False
    return a != b and b != c and a != c
