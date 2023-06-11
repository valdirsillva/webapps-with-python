from math import sqrt

def rootSquareSolver(a, b, c):
    if b*b - 4*a*c == 0:
        r1 = (-b+sqrt(b*b-4*a*c))/(2*a)
        
        return [r1]
    else:
        r1 = (-b+sqrt(b*b-4*a*c))/(2*a)
        r2 = (-b-sqrt(b*b-4*a*c))/(2*a)

        return [r1, r2]