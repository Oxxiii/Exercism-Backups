def isTriangle(sides):
    not_zero = (sides[0] > 0) and (sides[1] > 0) and (sides[2] > 0)
    triangle_inequality = sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]
    return not_zero and triangle_inequality

def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and isTriangle(sides)


def isosceles(sides):
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and isTriangle(sides)


def scalene(sides):
    
    return (not (equilateral(sides)) and not (isosceles(sides))) and isTriangle(sides)