from math import sqrt
from math import pi
from random import randint

patterns = []
# Creating global variables: 'direct_pattern' - String and 'patterns' - Array
possibilities = ["equals","is","matches","is equivalent to","is same as","is identical to","total up to","consists of"]

# Definition of function - counts factorial of given integer 'b'
def factorial():
    number = input("Factorial of what number: ")
    if(int(number) < 0):
        print("Type number bigger than 0.")
        factorial()
    else:
        result = 1
        try:
            number = int(number)
        except ValueError:
            print("Type number.")
            factorial()
        for i in range(1, number+1):
            result *= i
        print("Result of your factorial {}: {}".format(possibilities[possibility],result))

# Definition of function - counts circumference of any triangle
def triangle_calc():
    possibility = randint(0,7)
    triangle = str(input("Is your triangle equilateral or isosceles or different-sided?(e/i/d): "))
    if(triangle == "e" or triangle == "E"):
        side_length = int(input("Type side length of your triangle: "))
        tri_circ = side_length * 3
        print("Circumference of your triangle {}: {}".format(possibilities[possibility],tri_circ))
    elif(triangle.lower == "i"):
        tri_leg = int(input("Type legs length in your triangle: "))
        tri_base = int(input("Type base length in your triangle: "))
        tri_circ = tri_leg * 2 + tri_base
        print("Circumference of your triangle {}: {}".format(possibilities[possibility],tri_circ))
    elif(triangle.lower == "d"):
        tri_side1 = int(input("Type first side length in your triangle: "))
        tri_side2 = int(input("Type secord side length in your triangle: "))
        tri_side3 = int(input("Type third side length in your triangle: "))
        tri_circ = tri_side1 + tri_side2 + tri_side3
        print("Circumference of your triangle {}: {}".format(possibilities[possibility],tri_circ))
    else:
        print("Type correct letter: e or i or d")
        triangle_calc()

# Definition of function - counts area of rhombus with diagonals or with sides
def rhombus_calc():
    possibility = randint(0,7)
    diag_or_side = input("Formula with diagonals or with a side?(d/s)")
    if(diag_or_side.lower == "d"):
        rho_diag1 = int(input("Type first diagonal of your rhombus: "))
        rho_diag2 = int(input("Type second diagonal of your rhombus: "))
        rho_area = rho_diag1 * rho_diag2 / 2
        print("Area of your rhombus {}: {}".format(possibilities[possibility],rho_area))
    elif(diag_or_side.lower == "s"):
        side_length = int(input("Type side length of your rhombus: "))
        height = int(input("Type height of your rhombus: "))
        rho_area = side_length * height
        print("Area of your rhombus {}: {}".format(possibilities[possibility],rho_area))
    else:
        print("Type correct letter: d or s")
        rhombus_calc()

# Definition of function - counts circumference of any trapeze
def trapeze_calc():
    possibility = randint(0,7)
    is_isosceles = input("Is your trapeze isosceles or not? (y/n): ")
    if(is_isosceles == "y" or is_isosceles == "Y"):
        base_length1 = int(input("Type first base length of your trapeze: "))
        base_length2 = int(input("Type second base length of your trapeze: "))
        trap_leg = int(input("Type legs length in your trapeze: "))
        trap_circ = base_length1 + base_length2 + trap_leg * 2
    elif(is_isosceles == "n" or is_isosceles == "N"):
        base_length1 = int(input("Type first base length of your trapeze: "))
        base_length2 = int(input("Type second base length of your trapeze: "))
        trap_leg1 = int(input("Type first leg length in your trapeze: "))
        trap_leg2 = int(input("Type second leg length in your trapeze: "))
        trap_circ = base_length1 + base_length2 + trap_leg1 + trap_leg2
    else:
        print("Type correct letter: y or n")
        trapeze_calc()
    print("Circumference of your trapeze {}: {}".format(possibilities[possibility],trap_circ))

def calc():
    # Ask for question branch
    branch_of_science = int(input("Enter branch of your question: \nType 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics\n:"))
    if(branch_of_science == 1):
        categories = ["Basic Calculator","Geometry"]
        category = int(input("1 - {}\n2 - {}\nSelect one of those: ".format(*categories)))
        if(category == 1):
            patterns = ["Addition","Subtraction","Multiplication","Division","Power","Root","Modulo","Factorial"]
            def basic_calculator():  
                print("\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}\n8 - {}".format(*patterns))
                direct_pattern = int(input("Select one of above: "))
                possibility = randint(0,7)
                if(direct_pattern == 1):
                # Addiction
                    print("ADDICTION")
                    ingredient1 = int(input("Type first ingredient: "))
                    ingredient2 = int(input("Type second ingredient: "))
                    sum = ingredient1 + ingredient2
                    print("Sum of those numbers {}: {}".format(possibilities[possibility],sum))
                elif(direct_pattern == 2):
                # Subtraction
                    print("SUBTRACTION")
                    minuend = int(input("Type minuend: "))
                    subtrahend = int(input("Type subtrahend"))
                    difference = minuend - subtrahend
                    print("Difference of those numbers {}: {}".format(possibilities[possibility],difference))
                elif(direct_pattern == 3):
                # Multiplication
                    print("MULTIPLICATION")
                    factor1 = int(input("Type first factor: "))
                    factor2 = int(input("Type second factor: "))
                    product = factor1 * factor2
                    print("Product of those numbers {}: {}".format(possibilities[possibility],product))
                elif(direct_pattern == 4):
                # Division
                    print("DIVISION")
                    dividend = int(input("Type dividend: "))
                    divisor = int(input("Type divisor: "))
                    quotient = round(dividend / divisor,4)
                    remainder = dividend % divisor
                    floor_quotient = dividend // divisor
                    if(remainder != 0):
                        print(f"Quotient of those numbers {possibilities[possibility]}: {quotient} ({floor_quotient} and {remainder} remainder)")
                    else:
                        print(f"Quotient of those numbers {possibilities[possibility]} {quotient}")
                elif(direct_pattern == 5):
                # Power
                    print("POWER")
                    base = int(input("Type base: "))
                    exponent = int(input("Type exponent: "))
                    power = base ** exponent
                    if(power>0.001):
                        round(power,3)
                    print("Power of those numbers {}: {}".format(possibility,power))
                elif(direct_pattern == 8):
                # Factorial
                    print("FACTORIAL")
                    factorial()
                else:
                    print("Type correct number.")
        elif(category == 2):
            patterns = ["Square Diagonal","Square Area","Square Circumference","Rectangle Area","Rectangle Circumference","Triangle Area","Triangle Circumference","Rhombus Area","Rhombus Circumference","Parallelogram Area","Parallelogram Circumference","Trapeze Area","Trapeze Circumference","Circle Area","Circle Circumference","Cube Area","Cube Volume","Cuboid Area","Cuboid Volume","Cylinder Area","Cylinder Volume","Sphere Area","Sphere Volume"]
            print("\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n 7 - {}\n 8 - {}\n 9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}\n22 - {}\n23 - {}\n".format(*patterns))
            direct_pattern = int(input("Select one of above: "))
            possibility = randint(0,7)
            if(direct_pattern == 1):
            # Square diagonal
                print("SQUARE DIAGONAL")
                side_length = int(input("Type side length of your square: "))
                diagonal = round(side_length * sqrt(2),3)
                print("Diagonal of your square {}: {}√2 ({})".format(possibilities[possibility], side_length, diagonal))
            elif(direct_pattern == 2):
            # Square area
                print("SQUARE AREA")
                side_length = int(input("Type side lenght of your square: "))
                square_area = side_length ** 2
                print("Area of your square {}: {}".format(possibilities[possibility], square_area))
            elif(direct_pattern == 3):
            # Square circumference
                print("SQUARE CIRCUMFERENCE")
                side_length = int(input("Type side length of your square: "))
                square_circ = side_length * 4
                print("Circumference of your square {}: {}".format(possibilities[possibility], square_circ))
            elif(direct_pattern == 4):
            # Rectange area
                print("RECTANGLE AREA")
                rect_width = int(input("Type width of your rectangle: "))
                rect_height = int(input("Type height of your rectangle: "))
                rect_area = rect_height * rect_width
                print("Area of your rectangle {}: {}".format(possibilities[possibility], rect_area))
            elif(direct_pattern == 5):
            # Rectangle circumference
                print("RECTANGLE CIRCUMFERENCE")
                rect_width = int(input("Type width of your rectangle: "))
                rect_height = int(input("Type height of your rectangle: "))
                rect_circ = 2 * rect_width + 2 * rect_height
                print("Circumference of your rectangle {}: {}".format(possibilities[possibility], rect_circ))
            elif(direct_pattern == 6):
            # Triangle area
                print("TRIANGLE AREA")
                side_length = int(input("Type side length of your triangle: "))
                height = int(input("Type height of your triangle: "))
                tri_area = side_length * height / 2
                print("Area of your triangle {}: {}".format(possibilities[possibility], tri_area))
            elif(direct_pattern == 7):
            # Triangle circumference
                print("Triangle circumference")
                triangle_calc()
            elif(direct_pattern == 8):
            # Rhombus area
                print("RHOMBUS AREA")
                rhombus_calc()
            elif(direct_pattern == 9):
            # Rhombus circumference
                print("RHOMBUS CIRCUMFERENCE")
                side_length = int(input("Type side length of your rhombus: "))
                rho_circ = side_length * 4
                print("Circumference of your rhombus {}: {}".format(possibilities[possibility], rho_circ))
            elif(direct_pattern == 10):
            # Parallelogram area
                print("PARALLELOGRAM AREA")
                side_length = int(input("Type side length of your parallelogram: "))
                height = int(input("Type height of your parallelogram: "))
                par_area = side_length * height
                print("Area of your parallelogram {}: {}".format(possibilities[possibility], par_area))
            elif(direct_pattern == 11):
            # Parallelogram circumference
                print("PARALLELOGRAM CIRCUMFERENCE")
                side_length1 = int(input("Type first side length of your parallelogram: "))
                side_length2 = int(input("Type second side length of your parallelogram: "))
                par_circ = (side_length1 + side_length2) * 2
                print("Circumference of your parallelogram {}: {}".format(possibilities[possibility], par_circ))
            elif(direct_pattern == 12):
            # Trapeze area
                print("TRAPEZE AREA")
                base_length1 = int(input("Type first base length of your trapeze: "))
                base_length2 = int(input("Type second base length of your trapeze: "))
                height = int(input("Type height of your trapeze: "))
                trap_area = (base_length1 + base_length2) * height / 2
            elif(direct_pattern == 13):
            # Trapeze circumference
                print("TRAPEZE CIRCUMFERENCE")
                trapeze_calc()
            elif(direct_pattern == 14):
            # Circle area
                print("CIRCLE AREA")
                radius = int(input("Type radius of your circle (half of a diameter): "))
                cirl_area = round(radius**2 * pi, 4)
                print("Area of your circle {}: {}π ({})".format(possibilities[possibility], radius**2,cirl_area))
            elif(direct_pattern == 15):
            # Circle circumference
                print("CIRCLE CIRCUMFERENCE")
                radius = int(input("Type radius of your circle (half of a diameter): "))
                cirl_circ = round(radius * pi * 2, 4)
                print("Circumference of your circle {}: {}π ({})".format(possibilities[possibility], radius * 2,cirl_circ))
            elif(direct_pattern == 16):
            # Cube area
                print("CUBE AREA")
                edge_length = int(input("Type edge length of your cube: "))
                cube_area = edge_length**2 * 6
                print("Area of your cube {}: {}".format(possibilities[possibility], cube_area))
            elif(direct_pattern == 17):
            # Cube volume
                print("CUBE VOLUME")
                edge_length = int(input("Type edge length of your cube: "))
                cube_vol = edge_length**3
                print("Volume of your cube {}: {}".format(possibilities[possibility], cube_vol))
            elif(direct_pattern == 18):
            # Cuboid area
                print("CUBOID AREA")
                edge_length1 = int(input("Type first edge length of your cube: "))
                edge_length2 = int(input("Type second edge length of your cube: "))
                edge_length3 = int(input("Type third edge length of your cube: "))
                cuboid_area = (edge_length1 * edge_length2 + edge_length1 * edge_length3 + edge_length2 * edge_length3) * 2
                print("Area of your cuboid {}: {}".format(possibilities[possibility], cuboid_area))
            elif(direct_pattern == 19):
            # Cuboid volume
                print("CUBOID VOLUME")
                edge_length1 = int(input("Type first edge length of your cube: "))
                edge_length2 = int(input("Type second edge length of your cube: "))
                edge_length3 = int(input("Type third edge length of your cube: "))
                cuboid_vol = edge_length1 * edge_length2 * edge_length3
                print("Volume of your cuboid {}: {}".format(possibilities[possibility], cuboid_vol))
            elif(direct_pattern == 20):
            # Cylinder area
                print("CYLINDER AREA")
                radius = int(input("Type radius of your cylinder (half of a diameter): "))
                height = int(input("Type height of your cylinder: "))
                cyl_area = pi * radius * (radius + height) * 2
                print("Area of your cylinder {}: {}π ({})".format(possibilities[possibility], radius*(radius+height)*2,round(cyl_area)))
            elif(direct_pattern == 21):
            # Cylinder volume
                print("CYLINDER VOLUME")
                radius = int(input("Type radius of your cylinder (half of a diameter): "))
                height = int(input("Type height of your cylinder: "))
                cyl_vol = pi * radius**2 * height
                print("Volume of your cylinder {}: {}π ({})".format(possibilities[possibility], radius**2*height,round(cyl_vol,4)))
            elif(direct_pattern == 22):
            # Sphere area
                print("SPHERE AREA")
                radius = int(input("Type radius of your sphere (half of a diameter): "))
                sph_area = pi * radius**2 * 4
                print("Area of your sphere {}: {}π ({})".format(possibilities[possibility], radius**2*4,round(sph_area,4)))
            elif(direct_pattern == 23):
            # Sphere volume
                print("SPHERE VOLUME")
                radius = int(input("Type radius of your sphere (half of a diameter): "))
                sph_vol = pi * radius**3 * 4 / 3
                print("Volume of your sphere {}: {}π ({})".format(possibilities[possibility], radius**3*4/3,round(sph_vol,4)))
            else:
                print("This isn't currently available, but may be in future...")
                calc()
    elif(branch_of_science == 2):
        patterns = ["Density","Volume","Mass"]
        direct_pattern = int(input("Select one of those: \n1 - {}\n2 - {}\n3 - {}\n".format(*patterns)))
        if(direct_pattern == 1):
        # Density
            print("DENSITY")
            vol = int(input("Type volume: "))
            mass = int(input("Type mass: "))
            dens = round(mass / vol,4)
            print("Density is:",dens)
        elif(direct_pattern == 2):
        # Volume
            print("VOLUME")
            mass = int(input("Type mass: "))
            dens = int(input("Type density"))
            vol = round(mass / dens,4)
            print("Volume {}: {}".format(possibilities[possibility], vol))
        elif(direct_pattern == 3):
        # Mass
            print("MASS")
            vol = int(input("Type volume"))
            dens = int(input("Type density"))
            mass = vol * dens
            print("Mass {}: {}".format(possibilities[possibility], mass))
        else:
            print("Type correct number")
            calc()
    elif(branch_of_science == 3):
        patterns = ["Byte Calculator"]
        direct_pattern = int(input("Select one of those: \n1 - {}\n".format(*patterns)))
        if(direct_pattern == 1):
            print("It isn't currently availavle, sorry.")
            calc()
        else:
            print("Type correct number.")
    else:
       print("Type correct number")
       calc()
calc()