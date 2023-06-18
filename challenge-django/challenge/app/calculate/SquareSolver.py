from math import sqrt

def squareSolver(a, b, c):
    try:
        if b*b - 4*a*c == 0:
            r1 = (-b+sqrt(b*b-4*a*c))/(2*a)
            return [r1]
        else:
            r1 = (-b+sqrt(b*b-4*a*c))/(2*a)
            r2 = (-b-sqrt(b*b-4*a*c))/(2*a)
            r1 = f'{r1:.2g}'
            r2 = f'{r2:.2g}'
            return [r1, r2]
    except ValueError as e:
        print('Não foi possível realizar a operação')




        
              

