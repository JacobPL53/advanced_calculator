from math import sqrt, pi, prod
from random import choice

POSSIBS = (  
    'equals',
    'is',
    'matches',
    'is equivalent to',
    'is same as',
    'is identical to',
    'total up to',
    'consists of',
    'fits'
)
HEX_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

OCT_BIN = {
    '0': '000',
    '1': '001',
    '2': '010',
    '3': '011',
    '4': '100',
    '5': '101',
    '6': '110',
    '7': '111'
}

BIN_HEX = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
}

BIN_OCT = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}

BRANCH_OF_SCIENCE = (
    'Maths',
    'Chemistry',
    'Informatics'
)

PATTS = (
    (   
        'Addition',
        'Subtraction',
        'Multiplication',
        'Division',
        'Power',
        'Root',
        'Modulo',
        'Factorial'
    ),
    (
        'Square Diagonal',
        'Square Area',
        'Square Perimeter',
        'Rectangle Area',
        'Rectangle Perimeter',
        'Triangle Area',
        'Triangle Perimeter',
        'Rhombus Area',
        'Rhombus Perimeter',
        'Parallelogram Area',
        'Parallelogram Perimeter',
        'Trapeze Area',
        'Trapeze Perimeter',
        'Circle Area',
        'Circle Perimeter',
        'Cube Area',
        'Cube Volume',
        'Cuboid Area',
        'Cuboid Volume',
        'Cylinder Area',
        'Cylinder Volume',
        'Sphere Area',
        'Sphere Volume'
    ),
    (   
        'Mass',
        'Density',
        'Volume'
    ),
    (
        'Converting numbers to other number system',
        ''
    )
)
#==================
# USEFUL FUNCTIONS
#==================

def select(iter: tuple) -> None:
    """
        Prints all items from iterable as options to select
        @param iter: iterable containing the elements
    """
    x=''
    for i in range(0, len(iter)):
        x += f'\n{i+1} - {iter[i]}'
    print(x)

def unavai() -> None:
    """
        Used when function is in construction phase.
    """
    print('This isn\'t currently available, but may be in the future...')

def rnd_eq_syn() -> str:
    """
        Choices random synonym of word 'equal'.
        @returns: random string from POSSIBS.
    """
    return choice(POSSIBS)

def num_not_found(var: int) -> None:
    """
        Prints message saying that number isn't valid.
        @param var: variable containing the invalid number.
    """
    print(f'Provided number "{var}" doesn\'t match any of the proper numbers.')

#===========
# OPERATORS
#===========

def add() -> None:
    """
        Computes and prints sum of provided ingredients.
    """
    ingredients = (
        int(input('Type first ingredient: ')),
        int(input('Type second ingredient: '))
    )
    print('Sum of those numbers', rnd_eq_syn(), sum(ingredients))
    return sum(ingredients)

def sub() -> None:
    """
        Computes and prints difference of provided numbers.
    """
    minuend = int(input('Type minuend: '))
    subtrahend = int(input('Type subtrahend'))
    difference = minuend - subtrahend
    print('Difference of those numbers', rnd_eq_syn(), difference)
    return difference

def mult() -> None:
    """
        Computes and prints product of provided factors.
    """
    factors = (
        int(input('Type first factor: ')),
        int(input('Type second factor: '))
    )
    print('Product of those numbers', rnd_eq_syn(), prod(factors))
    return prod(factors)

def div() -> None:
    """
        Computes division of provided numbers. If remainder isn't equal 0, prints quotient and remainder.
        If it is, prints only quotient.
    """
    dividend = int(input('Type dividend: '))
    divisor = int(input('Type divisor: '))
    quotient = dividend / divisor
    remainder = dividend % divisor
    floor_quotient = dividend // divisor
    if(remainder != 0):
        print(f'Quotient of those numbers {rnd_eq_syn()} {quotient} ({floor_quotient} and {remainder} remainder)')
    else:
        print('Quotient of those numbers', rnd_eq_syn(), quotient)
    return quotient

def pow() -> None:
    """
        Computes and prints power with provided base and exponent.
    """
    base = int(input('Type base: '))
    exponent = int(input('Type exponent: '))
    power = base ** exponent
    print('Power of those number', rnd_eq_syn(), power)
    return power

def root() -> None:
    """
        Computes and prints root with provided radicand and index.
    """
    of_what_index = input('Root of what index: ')
    radicand = int(input('Type radicand: '))
    result = radicand ** (1/of_what_index)
    print('Result of your root', rnd_eq_syn(), result)
    return result

def mod() -> None:
    """
        Computes and prints remainder (modulo) of provided numbers.
    """
    dividend = int(input('Type dividend: '))
    divisor = int(input('Type divisor: '))
    remainder = dividend % divisor
    print('Modulo of those numbers', rnd_eq_syn(), remainder)
    return remainder

def fact() -> int:
    """
        Computes and prints factorial of provided number.
        @returns: 0 if provided number is negative.
    """
    try:
        of_what_num = int(input('Factorial of what number: '))
    except ValueError:
        print('Number provided by user is not an integer.')
        return 0
    else:
        if num > 0:
            old_num = num
            while old_num > 0:
                num *= old_num
                old_num -= 1
        else:
            print('Cannot count factorial from number smaller than 0.')
            return 0
        print('Result of your factorial', rnd_eq_syn(), num)
        return num

#==========
# GEOMETRY
#==========
def sqre_diag() -> None:
    """
        Computes and prints diagonal of square with provided length of side.
    """
    sd_len = int(input('Type side length of your square: '))
    diagonal = sd_len * sqrt(2)
    print(f'Diagonal of your square {rnd_eq_syn()} {sd_len}√2 ({diagonal})')
    return diagonal

def sqre_area() -> None:
    """
        Computes and prints area of square with provided length of side.
    """
    sd_len = int(input('Type side lenght of your square: '))
    square_area = sd_len ** 2
    print('Area of your square', rnd_eq_syn(), square_area)
    return square_area

def sqre_peri() -> None:
    """
        Computes and prints perimeter of square with provided length of side.
    """
    sd_len = int(input('Type side length of your square: '))
    sqre_peri = sd_len * 4
    print('Perimeter of your square', rnd_eq_syn(), sqre_peri)
    return sqre_peri

def rect_area() -> None:
    """
        Computes and prints area of rectangle with provided width and height.
    """
    rect_width = int(input('Type width of your rectangle: '))
    rect_height = int(input('Type height of your rectangle: '))
    rect_area = rect_height * rect_width
    print('Area of your rectangle', rnd_eq_syn(), rect_area)
    return rect_area

def rect_peri() -> None:
    """
        Computes and prints perimeter of rectangle with provided width and height.
    """
    rect_width = int(input('Type width of your rectangle: '))
    rect_height = int(input('Type height of your rectangle: '))
    rect_peri = 2 * (rect_width + rect_height)
    print('Perimeter of your rectangle', (rnd_eq_syn(), rect_peri))
    return rect_peri

def tria_area() -> None:
    """
        Computes and prints area of triangle with provided side length and height.
    """
    sd_len = int(input('Type side length of your triangle: '))
    height = int(input('Type height of your triangle: '))
    tri_area = sd_len * height / 2
    print('Area of your triangle', (rnd_eq_syn(), tri_area))
    return tri_area

def tria_peri() -> None:
    """
        Computes and prints perimeter of any triangle with provided side lengths.
    """
    triangle_type = input('Is your triangle equilateral or isosceles or different-sided?(e/i/d): ')
    if(triangle_type.lower() == 'e'):
        sd_len = int(input('Type side length of your triangle: '))
        tri_peri = sd_len * 3
        print('Perimeter of your triangle', rnd_eq_syn(), tri_peri)
    elif(triangle_type.lower() == 'i'):
        tri_leg = int(input('Type legs length in your triangle: '))
        tri_base = int(input('Type base length in your triangle: '))
        tri_peri = tri_leg * 2 + tri_base
        print('Perimeter of your triangle', rnd_eq_syn(), tri_peri)
    elif(triangle_type.lower() == 'd'):
        tri_sides = (
            int(input('Type first side length in your triangle: ')),
            int(input('Type second side length in your triangle: ')),
            int(input('Type third side length in your triangle: '))
        )
        tri_peri = sum(tri_sides)
        print('Perimeter of your triangle', rnd_eq_syn(), tri_peri)
    else:
        print(f'Provided letter \'{triangle_type}\' doesn\'t match any of the proper letters.')
        return 1
    return tri_peri

def rho_area() -> None:
    """
        Computes and prints area of rhombus using diagonals or side length provided by user.
    """
    diag_or_side = input('Formula with diagonals or with a side?(d/s)')
    if(diag_or_side.lower() == 'd'):
        rho_diags = (
            int(input('Type first diagonal of your rhombus: ')),
            int(input('Type second diagonal of your rhombus: '))
        )  
        rho_area = prod(rho_diags) / 2
        print('Area of your rhombus', rnd_eq_syn(), rho_area)
    elif(diag_or_side.lower() == 's'):
        sd_len = int(input('Type side length of your rhombus: '))
        height = int(input('Type height of your rhombus: '))
        rho_area = sd_len * height
        print('Area of your rhombus', rnd_eq_syn(), rho_area)
    else:
        print(f'Provided letter "{diag_or_side}" doesn\'t match any of the proper letters.')
        return 1
    return rho_area

def rho_peri() -> None:
    """
        Computes and prints perimeter of rhombus with provided side length.
    """
    sd_len = int(input('Type side length of your rhombus: '))
    rho_peri = sd_len * 4
    print('Perimeter of your rhombus', rnd_eq_syn(), rho_peri)
    return rho_peri

def par_area() -> None:
    """
        Computes and prints area of parallel with provided side length and height.
    """
    sd_len = int(input('Type side length of your parallelogram: '))
    height = int(input('Type height of your parallelogram: '))
    par_area = sd_len * height
    print('Area of your parallelogram', rnd_eq_syn(), par_area)
    return par_area

def par_peri() -> None:
    """
        Computes and prints perimeter of parallel with provided side lengths.
    """
    sides = (
        int(input('Type first side length of your parallelogram: ')),
        int(input('Type second side length of your parallelogram: '))
    )
    par_peri = sum(sides) * 2
    print('Perimeter of your parallelogram', rnd_eq_syn(), par_peri)
    return par_peri

def trap_area() -> None:
    """
        Computes and prints area of trapeze with provided bases and height.
    """
    bases = (
        int(input('Type first base length of your trapeze: ')),
        int(input('Type second base length of your trapeze: '))
    )
    height = int(input('Type height of your trapeze: '))
    trap_area = sum(bases) * height / 2
    print('Area of your trapeze', rnd_eq_syn(), trap_area)
    return trap_area

def trap_peri() -> None:
    """
        Computes and prints perimeter of any trapeze using provided side lengths.
    """
    is_isosceles = input('Is your trapeze isosceles or not? (y/n): ')
    if(is_isosceles.lower() == 'y'):
        base_lengths = (
            int(input('Type first base length of your trapeze: ')),
            int(input('Type second base length of your trapeze: '))
        )
        trap_leg = int(input('Type legs length in your trapeze: '))
        trap_peri = sum(base_lengths) + trap_leg * 2
        print('Perimeter of your trapeze', rnd_eq_syn(), trap_peri)
    elif(is_isosceles.lower() == 'n'):
        base_lengths = (
            int(input('Type first base length of your trapeze: ')),
            int(input('Type second base length of your trapeze: '))
        )
        trap_legs = (
            int(input('Type first leg length in your trapeze: ')),
            int(input('Type second leg length in your trapeze: '))
        )
        trap_peri = sum(sum(base_lengths),(trap_legs))
        print('Perimeter of your trapeze', rnd_eq_syn(), trap_peri)
    else:
        print(f'Provided letter "{is_isosceles}" doesn\'t match any of the proper letters.')
        return 1
    return trap_peri

def circ_area() -> None:
    """
        Computes and prints area of circle with provided radius.
    """
    radius = int(input('Type radius of your circle (half of a diameter): '))
    without_pi = radius**2
    circ_area = pi * without_pi
    print(f'Area of your circle {rnd_eq_syn()} {without_pi}π ({circ_area})')
    return circ_area

def circ_peri() -> None:
    """
        Computes and prints perimeter of circle with provided radius.
    """
    radius = int(input('Type radius of your circle (half of a diameter): '))
    without_pi = radius * 2
    circ_peri = pi * without_pi
    print(f'Perimeter of your circle {rnd_eq_syn()} {without_pi}π ({circ_peri})')
    return circ_peri

def cube_area() -> None:
    """
        Computes and prints area of cube with provided edge length.
    """
    edge_length = int(input('Type edge length of your cube: '))
    cube_area = edge_length**2 * 6
    print('Area of your cube', rnd_eq_syn(), cube_area)
    return cube_area

def cube_vol() -> None:
    """
        Computes and prints volume of cube with provided edge length.
    """
    edge_length = int(input('Type edge length of your cube: '))
    cube_vol = edge_length**3
    print('Volume of your cube', rnd_eq_syn(), cube_vol)
    return cube_vol

def cubo_area() -> None:
    """
        Computes and prints area of cuboid with provided edge lengths.
    """
    edge_lengths = (
        int(input('Type first edge length of your cube: ')),
        int(input('Type second edge length of your cube: ')),
        int(input('Type third edge length of your cube: '))
    )
    cubo_area = (edge_lengths[0] * edge_lengths[1] + edge_lengths[0] * edge_lengths[2] + edge_lengths[1] * edge_lengths[2]) * 2
    print('Area of your cuboid', rnd_eq_syn(), cubo_area)
    return cubo_area

def cubo_vol() -> None:
    """
        Computes and prints volume of cuboid with provided edge lengths.
    """
    edge_lengths = (
        int(input('Type first edge length of your cube: ')),
        int(input('Type second edge length of your cube: ')),
        int(input('Type third edge length of your cube: '))
    )
    cuboid_vol = prod(edge_lengths)
    print('Volume of your cuboid', rnd_eq_syn(), cuboid_vol)
    return cubo_vol

def cyl_area() -> None:
    """
        Computes and prints area of cylinder with provided radius and height.
    """
    radius = int(input('Type radius of your cylinder (half of a diameter): '))
    height = int(input('Type height of your cylinder: '))
    without_pi = radius * (radius + height) * 2
    cyl_area = pi * without_pi
    print(f'Area of your cylinder {rnd_eq_syn()} {without_pi}π ({cyl_area})')
    return cyl_area

def cyl_vol() -> None:
    """
        Computes and prints volume of cylinder with provided radius and height.
    """
    radius = int(input('Type radius of your cylinder (half of a diameter): '))
    height = int(input('Type height of your cylinder: '))
    without_pi = radius**2 * height
    cyl_vol = pi * without_pi
    print(f'Volume of your cylinder {rnd_eq_syn()} {without_pi}π ({cyl_vol})')
    return cyl_vol

def sph_area() -> None:
    """
        Computes and prints area of sphere with provided radius.
    """
    radius = int(input('Type radius of your sphere (half of a diameter): '))
    without_pi = radius**2 * 4
    sph_area = pi * without_pi
    print(f'Area of your sphere {rnd_eq_syn()} {without_pi}π ({sph_area})')
    return sph_area

def sph_vol() -> None:
    """
        Computes and prints volume of sphere with provided radius.
    """
    radius = int(input('Type radius of your sphere (half of a diameter): '))
    without_pi = radius**3 * 4 / 3
    sph_vol = pi * without_pi
    print(f'Volume of your sphere {rnd_eq_syn()} {without_pi}π ({sph_vol})')
    return sph_vol

#==========
# CHEMISTS
#==========

def dens() -> None:
    """
        Computes and prints density of an object with provided volume and mass.
    """
    vol = int(input('Type volume: '))
    mass = int(input('Type mass: '))
    dens = mass / vol
    print('Density', rnd_eq_syn(), dens)
    return dens

def vol() -> None:
    """
        Computes and prints volume of an object with provided mass and density.
    """
    mass = int(input('Type mass: '))
    dens = int(input('Type density: '))
    vol = mass / dens
    print('Volume', rnd_eq_syn(), vol)
    return vol

def mass() -> None:
    """
        Computes and prints mass of an object with provided volume and density.
    """
    vol = int(input('Type volume: '))
    dens = int(input('Type density: '))
    mass = vol * dens
    print('Mass', rnd_eq_syn(), mass)
    return mass


#=============
# INFORMATICS
#=============


def dec_to_bin(dec: int) -> str:
    """
        Converts provided decimal number to binary.
        @param dec: decimal number, which will be converted.
        @returns: the same number in binary system.
    """
    dec = int(dec)
    if(dec>0):
        bin = ''
        i = 1
        while(dec>0):
            bin += str(dec % 2)
            dec //= 2
        return bin[::-1]
    else:
        return 'Neither decimal or binary number can be equal zero or smaller here.'

def hex_to_bin(hex: int) -> str:
    """
        Converts provided hexadecimal number to binary.
        @param hex: hexadecimal number, which will be converted.
        @returns: the same number in binary system.
    """
    hexs = str(hex)
    bin = ''
    for i in range(len(hexs)):
        bin += HEX_BIN[hexs[i]]
    return bin

def oct_to_bin(oct: int) -> str:
    """
        Converts provided octal number to binary.
        @param oct: octal number, which will be converted.
        @returns: the same number in binary system.
    """
    oct = str(oct)
    bin = ''
    for i in range(len(oct)):
        bin += OCT_BIN[oct[i]]
    return bin

def bin_to_dec(bin: int) -> str:
    """
        Converts provided binary number to decimal.
        @param bin: binary number, which will be converted.
        @returns: the same number in decimal system.
    """
    expo = 1
    dec = 0
    bin = str(bin)
    for i in range(len(bin)-1):
        if(bin[i] == 1):
            dec += expo
            expo *= 2
    return dec[::-1]

def bin_to_hex(bin: int) -> str:
    """
        Converts provided binary number to hexadecimal.
        @param bin: binary number, which will be converted.
        @returns: the same number in hexadecimal system.
    """
    hex = ''
    bins = str(bin)
    lb = len(bins)
    if lb % 4 != 0:
        bin = str(bins.zfill((lb//4 + 1) * 4))
    for i in range(lb):
        if(i % 4 == 0):
            hex += BIN_HEX[str(bin[i]) + str(bin[i+1]) + str(bin[i+2]) + str(bin[i+3])]
    return hex

def bin_to_oct(bin: int) -> str:
    """
        Converts provided binary number to octal.
        @param bin: binary number, which will be converted.
        @returns: the same number in octal system.
    """
    oct = ''
    bins = str(bin)
    lb = len(bins)
    if lb % 3 != 0:
        bin = str(bins.zfill((lb//3 + 1) * 3))
    for i in range(lb):
        if(i % 3 == 0):
            oct += BIN_OCT[str(bin[i]) + str(bin[i+1]) + str(bin[i+2])]
    return oct

def convert(sys1: str, sys2: str, num: int) -> str:
    """
        Numerical system convertion manager.
        @param sys1: first system - that one, in which provided number is.
        @param sys2: second system - that one, to which you want to convert.
        @param num: number to convert.
        @returns: number converted to another number system.
    """
    if sys2 != sys1:
        try:
            if sys2 == 'b':
                if sys1 == 'o':
                    return oct_to_bin(num)
                elif sys1 == 'd':
                    return dec_to_bin(num)
                else:
                    return hex_to_bin(num)
            elif sys2 == 'o':
                if sys1 == 'b':
                    return bin_to_oct(num)
                elif sys1 == 'd':
                    return bin_to_oct(dec_to_bin(num))
                else:
                    return bin_to_oct(hex_to_bin(num))
            elif sys2 == 'd':
                if sys1 == 'b':
                    return bin_to_dec(num)
                elif sys1 == 'o':
                    return bin_to_dec(oct_to_bin(num))
                else:
                    return bin_to_dec(hex_to_bin(num))
            elif sys2 == 'h':
                if sys1 == 'b':
                    return bin_to_hex(num)
                elif sys1 == 'o':
                    return bin_to_hex(oct_to_bin(num))
                else:
                    return bin_to_hex(dec_to_bin(num))
            else:
                num_not_found(sys2)
        except KeyError:
            fsys = 'binary' if sys1 == 'b' else ('octal' if sys1 == 'o' else ('decimal' if sys1 == 'd' else 'hexadecimal'))
            return "Provided number " + num + " doesn't match " + fsys + " number system."
    else:
        return 'You want to convert number to the same number system.'