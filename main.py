from patterns import *
from math import sqrt
from math import pi
from random import randint

def factorial():
    number = input('Factorial of what number: ')
    if(int(number) < 0):
        print('Type number bigger than 0.')
        factorial()
    else:
        result = 1
        try:
            number = int(number)
        except ValueError:
            print('Type number.')
            factorial()
        for i in range(1, number+1):
            result *= i
        print('Result of your factorial', rnd_eq_syn(),result)

def calc():
    # Ask for question branch
    print('Type 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics')
    branch_of_science = int(input('Select one of above: '))
    if(branch_of_science == 1):
        categories = ['Basic Calculator','Geometry']
        category = int(input('1 - {}\n2 - {}\nSelect one of those: '.format(*categories)))
        if(category == 1):
            direct_pattern = int(input('Select one of above: \n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n8 - {}').format(*patts[0]))
            if(direct_pattern == 1):
                addition()
            elif(direct_pattern == 2):
                subtraction()
            elif(direct_pattern == 3):
                multiplication()
            elif(direct_pattern == 4):
                division()
            elif(direct_pattern == 5):
                power()
            elif(direct_pattern == 6):
                root()
            elif(direct_pattern == 7):
                modulo()
            elif(direct_pattern == 8):
                factorial()
            else:
                print(f'Provided number "{direct_pattern}" doesn\'t match any of the proper numbers.')
        elif(category == 2):
            # print(f'\n{n} - '.join(list(map(lambda n: patts[1][n],list([i for i in range(0, len(patts[1]))])))))
            print('\n1 - {}\n2 - {}\n 3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n8 - {}\n9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}\n22 - {}\n23 - {}'.format(*patts[1]))
            direct_pattern = int(input('Select one of above: '))
            if(direct_pattern == 1):
                sqre_diag()
            elif(direct_pattern == 2):
                sqre_area()
            elif(direct_pattern == 3):
                sqre_peri()
            elif(direct_pattern == 4):
                rect_area()
            elif(direct_pattern == 5):
                rect_peri()
            elif(direct_pattern == 6):
                tria_area()
            elif(direct_pattern == 7):
                tria_peri()
            elif(direct_pattern == 8):
                rho_area()
            elif(direct_pattern == 9):
                rho_peri()
            elif(direct_pattern == 10):
                par_area()
            elif(direct_pattern == 11):
                par_peri()
            elif(direct_pattern == 12):
                trap_area()
            elif(direct_pattern == 13):
                trap_peri()
            elif(direct_pattern == 14):
                circ_area()
            elif(direct_pattern == 15):
                circ_peri()
            elif(direct_pattern == 16):
                cube_area()
            elif(direct_pattern == 17):
                cube_vol()
            elif(direct_pattern == 18):
                cubo_area()
            elif(direct_pattern == 19):
                cubo_vol()
            elif(direct_pattern == 20):
                cyl_area()
            elif(direct_pattern == 21):
                cyl_vol()
            elif(direct_pattern == 22):
                sph_area()
            elif(direct_pattern == 23):
                sph_vol()
            else:
                print(f'Provided number "{direct_pattern}" doesn\'t match any of the proper numbers.')
        else:
            print(f'Provided number "{category}" doesn\'t match any of the proper numbers.')
    elif(branch_of_science == 2):
        direct_pattern = int(input('Select one of those: \n1 - {}\n2 - {}\n3 - {}\n'.format(*patts[2])))
        if(direct_pattern == 1):
            dens()
        elif(direct_pattern == 2):
            vol()
        elif(direct_pattern == 3):
            mass()
        else:
            print(f'Provided number "{direct_pattern}" doesn\'t match any of the proper numbers.')
    elif(branch_of_science == 3):
        direct_pattern = int(input('Select one of those: \n1 - {}\n2 - {}\n'.format(*patts[3])))
        if(direct_pattern == 1):
            print('It isn\'t currently availavle, sorry.')
        elif(direct_pattern == 2):
            print('It isn\'t currently availavle, sorry.')
        else:
            print(f'Provided number "{direct_pattern}" doesn\'t match any of the proper numbers.')
    else:
       print(f'Provided number "{branch_of_science}" doesn\'t match any of the proper numbers.')
calc()