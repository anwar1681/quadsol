import os

def eqnsol1():
    print('\nax^2 +bx + c = 0')
    print()
    a = int(input('enter value of a: '))
    b = int(input('enter value of b: '))
    c = int(input('enter value of c: '))
    print(f'\n{a}*x^2 + {b}*x + {c} = 0\n')
    D = (b**2 - 4*a*c)**0.5
    x1 = round((-b + D)/(2*a),2)
    x2 = round((-b - D)/(2*a),2)
    print(f'First root of the eqn X1: {x1}')
    print(f'Second root of the eqn X2: {x2}')
    return x1, x2

if __name__ =='__main__':
    eqnsol1()
