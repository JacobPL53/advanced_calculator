from patterns import *

CATEGORIES = (
    'Basic Calculator',
    'Geometry'
)

select(BRANCH_OF_SCIENCE)
branch_of_science = int(input('Select one of above: '))
if(branch_of_science == 1):
    select(CATEGORIES)
    category = int(input('Select one of above: '))
    if(category == 1):
        select(PATTS[0])
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
        select(PATTS[1])
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
    select(PATTS[2])
    direct_pattern = int(input('Select one of above: '))
    if(direct_pattern == 1):
        dens()
    elif(direct_pattern == 2):
        vol()
    elif(direct_pattern == 3):
        mass()
    else:
        num_not_found(direct_pattern)
elif(branch_of_science == 3):
    select(PATTS[3])
    direct_pattern = int(input('Select one of above: '))
    if(direct_pattern == 1):
        sys1 = input('In which system your number is? (b/o/d/h): ')
        if sys1 != 'b' and sys1 != 'o' and sys1 != 'd' and sys1 != 'h':
            num_not_found(sys1)
        sys2 = input('To which system do you want to convert? (b/o/d/h): ')
        if sys2 != 'b' and sys2 != 'o' and sys2 != 'd' and sys2 != 'h':
            num_not_found(sys2)
        num = input('Enter your number: ')
        print(convert(sys1, sys2, num))
    elif(direct_pattern == 2):
        unavai()
    else:
        num_not_found(direct_pattern)
else:
    num_not_found(branch_of_science)