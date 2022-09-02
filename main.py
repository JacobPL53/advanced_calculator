from patterns import *

CATEGORIES = (
    'Basic Calculator',
    'Geometry'
)

# Ask for question branch
print('Type 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics')
branch_of_science = int(input('Select one of above: '))
if(branch_of_science == 1):
    category = int(input('1 - {}\n2 - {}\nSelect one of those: '.format(*CATEGORIES)))
    if(category == 1):
        print('\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n8 - {}'.format(*PATTS[0]))
        direct_pattern = int(input('Select one of above: '))
        if(direct_pattern == 1):
            add()
        elif(direct_pattern == 2):
            sub()
        elif(direct_pattern == 3):
            mult()
        elif(direct_pattern == 4):
            div()
        elif(direct_pattern == 5):
            pow()
        elif(direct_pattern == 6):
            root()
        elif(direct_pattern == 7):
            mod()
        elif(direct_pattern == 8):
            fact()
        else:
            num_not_found(direct_pattern)
    elif(category == 2):
        # print(f'\n{n} - '.join(list(map(lambda n: patts[1][n],list([i for i in range(0, len(patts[1]))])))))
        print('\n1 - {}\n2 - {}\n 3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n8 - {}\n9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}\n22 - {}\n23 - {}'.format(*PATTS[1]))
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
            num_not_found(direct_pattern)
    else:
        num_not_found(category)
elif(branch_of_science == 2):
    direct_pattern = int(input('Select one of those: \n1 - {}\n2 - {}\n3 - {}\n'.format(*PATTS[2])))
    if(direct_pattern == 1):
        dens()
    elif(direct_pattern == 2):
        vol()
    elif(direct_pattern == 3):
        mass()
    else:
        num_not_found(direct_pattern)
elif(branch_of_science == 3):
    direct_pattern = int(input('Select one of those: \n1 - {}\n2 - {}\n'.format(*PATTS[3])))
    if(direct_pattern == 1):
        unavai()
    elif(direct_pattern == 2):
        unavai()
    else:
        num_not_found(direct_pattern)
else:
    num_not_found(branch_of_science)