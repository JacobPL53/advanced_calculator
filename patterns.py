from math import sqrt
from math import pi
from random import choice

possib = (  
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

patts = (
    (   'Addition',
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
    (   'Mass',
        'Density',
        'Volume'
    ),
    (   'Byte Calculator',
        'Converting numbers to other number system'
    )
)
def mult(*args) -> int:
    res = 1
    for num in args:
        res *= num
    return res

def unavai() -> None:
    print('This isn\'t currently available, but may be in the future...')

def rnd_eq_syn() -> object:
    return choice(possib)

def addition() -> None:
    ingredients = (
        int(input('Type first ingredient: ')),
        int(input('Type second ingredient: '))
    )
    print('Sum of those numbers', rnd_eq_syn(), sum(ingredients))

def subtraction() -> None:
    minuend = int(input('Type minuend: '))
    subtrahend = int(input('Type subtrahend'))
    difference = minuend - subtrahend
    print('Difference of those numbers', rnd_eq_syn(), difference)

def multiplication() -> None:
    factors = (
        int(input('Type first factor: ')),
        int(input('Type second factor: '))
    )
    print('Product of those numbers', rnd_eq_syn(), factors(0) * factors(1))

def division() -> None:
    dividend = int(input('Type dividend: '))
    divisor = int(input('Type divisor: '))
    quotient = dividend / divisor
    remainder = dividend % divisor
    floor_quotient = dividend // divisor
    if(remainder != 0):
        print(f'Quotient of those numbers {rnd_eq_syn()} {quotient} ({floor_quotient} and {remainder} remainder)')
    else:
        print('Quotient of those numbers', rnd_eq_syn(), quotient)

def power() -> None:
    base = int(input('Type base: '))
    exponent = int(input('Type exponent: '))
    power = base ** exponent
    print('Power of those number', rnd_eq_syn(), power)

def root() -> None:
    type_of_root = input('Square or cube root? (s/c)')
    if(type_of_root.lower() == 's'):
        radicand = int(input('Type radicand: '))
        result = sqrt(radicand)
    elif(type_of_root.lower() == 'c'):
        radicand - int(input('Type radicand: '))
        result = radicand ** (1/3)
    print('Result of your root', rnd_eq_syn(), result)

def modulo() -> None:
    dividend = int(input('Type dividend: '))
    divisor = int(input('Type divisor: '))
    remainder = dividend % divisor
    print('Modulo of those numbers', rnd_eq_syn(), remainder)

def factorial() -> int:
    try:
        text = input('Factorial of what number: ')
        num = int(text)
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

def sqre_diag() -> None:
    sd_len = int(input('Type side length of your square: '))
    diagonal = sd_len * sqrt(2)
    print('Diagonal of your square {} {}√2 ({})'.format(rnd_eq_syn(), sd_len, diagonal))

def sqre_area() -> None:
    sd_len = int(input('Type side lenght of your square: '))
    square_area = sd_len ** 2
    print('Area of your square', rnd_eq_syn(), square_area)

def sqre_peri() -> None:
    sd_len = int(input('Type side length of your square: '))
    square_peri = sd_len * 4
    print('Perimeter of your square', rnd_eq_syn(), square_peri)

def rect_area() -> None:
    rect_width = int(input('Type width of your rectangle: '))
    rect_height = int(input('Type height of your rectangle: '))
    rect_area = rect_height * rect_width
    print('Area of your rectangle', rnd_eq_syn(), rect_area)

def rect_peri() -> None:
    rect_width = int(input('Type width of your rectangle: '))
    rect_height = int(input('Type height of your rectangle: '))
    rect_peri = 2 * rect_width + 2 * rect_height
    print('Perimeter of your rectangle', (rnd_eq_syn(), rect_peri))

def tria_area() -> None:
    sd_len = int(input('Type side length of your triangle: '))
    height = int(input('Type height of your triangle: '))
    tri_area = sd_len * height / 2
    print('Area of your triangle', (rnd_eq_syn(), tri_area))

def tria_peri() -> None:
    triangle = input('Is your triangle equilateral or isosceles or different-sided?(e/i/d): ')
    if(triangle.lower() == 'e'):
        sd_len = int(input('Type side length of your triangle: '))
        tri_peri = sd_len * 3
        print('Perimeter of your triangle', rnd_eq_syn(), tri_peri)
    elif(triangle.lower() == 'i'):
        tri_leg = int(input('Type legs length in your triangle: '))
        tri_base = int(input('Type base length in your triangle: '))
        tri_peri = tri_leg * 2 + tri_base
        print('Perimeter of your triangle', rnd_eq_syn(), tri_peri)
    elif(triangle.lower() == 'd'):
        tri_sides = (
            int(input('Type first side length in your triangle: ')),
            int(input('Type second side length in your triangle: ')),
            int(input('Type third side length in your triangle: '))
        )
        tri_peri = sum(tri_sides)
        print('Perimeter of your triangle', rnd_eq_syn(), tri_peri)
    else:
        print(f'Provided letter \'{triangle}\' doesn\'t match any of the proper letters.')

def rho_area() -> None:
    diag_or_side = input('Formula with diagonals or with a side?(d/s)')
    if(diag_or_side.lower() == 'd'):
        rho_diags = (
            int(input('Type first diagonal of your rhombus: ')),
            int(input('Type second diagonal of your rhombus: '))
        )  
        rho_area = mult(rho_diags) / 2
        print('Area of your rhombus', rnd_eq_syn(), rho_area)
    elif(diag_or_side.lower() == 's'):
        sd_len = int(input('Type side length of your rhombus: '))
        height = int(input('Type height of your rhombus: '))
        rho_area = sd_len * height
        print('Area of your rhombus', rnd_eq_syn(), rho_area)
    else:
        print(f'Provided letter "{diag_or_side}" doesn\'t match any of the proper letters.')

def rho_peri() -> None:
    sd_len = int(input('Type side length of your rhombus: '))
    rho_peri = sd_len * 4
    print('Perimeter of your rhombus', rnd_eq_syn(), rho_peri)

def par_area() -> None:
    sd_len = int(input('Type side length of your parallelogram: '))
    height = int(input('Type height of your parallelogram: '))
    par_area = sd_len * height
    print('Area of your parallelogram', rnd_eq_syn(), par_area)

def par_peri() -> None:
    sides = (
        int(input('Type first side length of your parallelogram: ')),
        int(input('Type second side length of your parallelogram: '))
    )
    par_peri = sum(sides) * 2
    print('Perimeter of your parallelogram', rnd_eq_syn(), par_peri)

def trap_area() -> None:
    bases = (
        int(input('Type first base length of your trapeze: ')),
        int(input('Type second base length of your trapeze: '))
    )
    height = int(input('Type height of your trapeze: '))
    trap_area = sum(bases) * height / 2

def trap_peri() -> None:
    is_isosceles = input('Is your trapeze isosceles or not? (y/n): ')
    if(is_isosceles.lower() == 'y'):
        base_lengths = (
            int(input('Type first base length of your trapeze: ')),
            int(input('Type second base length of your trapeze: '))
        )
        trap_leg = int(input('Type legs length in your trapeze: '))
        trap_peri = sum(base_lengths) + trap_leg * 2
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
    else:
        print(f'Provided letter "{is_isosceles}" doesn\'t match any of the proper letters.')
    print('Perimeter of your trapeze', rnd_eq_syn(), trap_peri)

def circ_area() -> None:
    radius = int(input('Type radius of your circle (half of a diameter): '))
    circ_area = pi * radius**2
    print(f'Area of your circle {rnd_eq_syn()} {radius**2}π ({circ_area})')

def circ_peri() -> None:
    radius = int(input('Type radius of your circle (half of a diameter): '))
    circ_peri = 2 * pi * radius
    print(f'Perimeter of your circle {rnd_eq_syn()} {radius * 2}π ({circ_peri})')

def cube_area() -> None:
    edge_length = int(input('Type edge length of your cube: '))
    cube_area = edge_length**2 * 6
    print('Area of your cube', rnd_eq_syn(), cube_area)

def cube_vol() -> None:
    edge_length = int(input('Type edge length of your cube: '))
    cube_vol = edge_length**3
    print('Volume of your cube', rnd_eq_syn(), cube_vol)

def cubo_area() -> None:
    edge_lengths = (
        int(input('Type first edge length of your cube: ')),
        int(input('Type second edge length of your cube: ')),
        int(input('Type third edge length of your cube: '))
    )
    # Try to simplify this
    cuboid_area = (edge_lengths(0) * edge_lengths(1) + edge_lengths(0) * edge_lengths(2) + edge_lengths(1) * edge_lengths(2)) * 2
    print('Area of your cuboid', rnd_eq_syn(), cuboid_area)

def cubo_vol() -> None:
    edge_lengths = (
        int(input('Type first edge length of your cube: ')),
        int(input('Type second edge length of your cube: ')),
        int(input('Type third edge length of your cube: '))
    )
    cuboid_vol = mult(edge_lengths)
    print('Volume of your cuboid', rnd_eq_syn(), cuboid_vol)

def cyl_area() -> None:
    radius = int(input('Type radius of your cylinder (half of a diameter): '))
    height = int(input('Type height of your cylinder: '))
    cyl_area = pi * radius * (radius + height) * 2
    print(f'Area of your cylinder {rnd_eq_syn()} {radius * (radius + height) * 2}π ({cyl_area})')

def cyl_vol() -> None:
    radius = int(input('Type radius of your cylinder (half of a diameter): '))
    height = int(input('Type height of your cylinder: '))
    cyl_vol = pi * radius**2 * height
    print(f'Volume of your cylinder {rnd_eq_syn()} {radius**2 * height}π ({cyl_vol})')

def sph_area() -> None:
    radius = int(input('Type radius of your sphere (half of a diameter): '))
    sph_area = pi * radius**2 * 4
    print(f'Area of your sphere {rnd_eq_syn()} {radius**2 * 4}π ({sph_area})')

def sph_vol() -> None:
    radius = int(input('Type radius of your sphere (half of a diameter): '))
    sph_vol = pi * radius**3 * 4 / 3
    print(f'Volume of your sphere {rnd_eq_syn()} {radius**3 * 4 / 3}π ({sph_vol})')

def dens() -> None:
    vol = int(input('Type volume: '))
    mass = int(input('Type mass: '))
    dens = mass / vol
    print('Density is:',dens)

def vol() -> None:
    mass = int(input('Type mass: '))
    dens = int(input('Type density'))
    vol = mass / dens
    print('Volume', rnd_eq_syn(), vol)

def mass() -> None:
    vol = int(input('Type volume'))
    dens = int(input('Type density'))
    mass = vol * dens
    print('Mass', rnd_eq_syn(), mass)