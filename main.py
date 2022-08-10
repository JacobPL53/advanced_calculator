import math
# Creating global variables: 'direct_pattern' - String and 'patterns' - Array
direct_pattern = ""
patterns = []
def triangle_calc():
    triangle = str(input("Is your triangle equilateral or isosceles or different-sided?(e/i/d): "))
    if(triangle == "e" or triangle == "E"):
        side_length = int(input("Type side length of your triangle: "))
        tri_circ = side_length * 3
        print("Circumference of your triangle is: {}".format(tri_circ))
    elif(triangle.lower == "i"):
        tri_leg = int(input("Type legs length in your triangle: "))
        tri_base = int(input("Type base length in your triangle: "))
        tri_circ = tri_leg * 2 + tri_base
        print("Circumference of your triangle is: {}".format(tri_circ))
    elif(triangle.lower == "d"):
        tri_side1 = int(input("Type first side length in your triangle: "))
        tri_side2 = int(input("Type secord side length in your triangle: "))
        tri_side3 = int(input("Type third side length in your triangle: "))
        tri_circ = tri_side1 + tri_side2 + tri_side3
        print("Circumference of your triangle is: {}".format(tri_circ))
    else:
        print("Type correct letter: e or i or d")
        triangle_calc()
def rhombus_calc():
    diag_or_side = input("Formula with diagonals or with a side?(d/s)")
    if(diag_or_side.lower == "d"):
        rho_diag1 = int(input("Type first diagonal of your rhombus: "))
        rho_diag2 = int(input("Type second diagonal of your rhombus: "))
        rho_area = rho_diag1 * rho_diag2 / 2
        print("Area of your rhombus is: {}".format(rho_area))
    elif(diag_or_side.lower == "s"):
        side_length = int(input("Type side length of your rhombus: "))
        height = int(input("Type height of your rhombus: "))
        rho_area = side_length * height
        print("Area of your rhombus is: {}".format(rho_area))
    else:
        print("Type correct letter: d or s")
        rhombus_calc()
def TrapezeCalc():
    IsIsosceles = input("Is your trapeze isosceles or not? (y/n): ")
    if(IsIsosceles == "y" or IsIsosceles == "Y"):
        BaseLength1 = int(input("Type first base length of your trapeze: "))
        BaseLength2 = int(input("Type second base length of your trapeze: "))
        TrapLeg = int(input("Type legs length in your trapeze: "))
        TrapCirc = BaseLength1 + BaseLength2 + TrapLeg * 2
    elif(IsIsosceles == "n" or IsIsosceles == "N"):
        BaseLength1 = int(input("Type first base length of your trapeze: "))
        BaseLength2 = int(input("Type second base length of your trapeze: "))
        TrapLeg1 = int(input("Type first leg length in your trapeze: "))
        TrapLeg2 = int(input("Type second leg length in your trapeze: "))
        TrapCirc = BaseLength1 + BaseLength2 + TrapLeg1 + TrapLeg2
    else:
        print("Type correct letter: y or n")
        TrapezeCalc()
    print("Circumference of your trapeze is: {}".format(TrapCirc))
    
def Calc():
    # Ask for question branch
    branchOfScience = int(input("Enter branch of your question: \nType 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics\n:"))
    if(branchOfScience == 1):
        categories = ["Basic Calculator","Geometry"]
        category = int(input("1 - {}\n2 - {}\nSelect one of those: ".format(*categories)))
        if(category == 1):
            patterns = ["Addition","Subtraction","Multiplication","Division","Power","Root","Modulo"]
            print("\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n6 - {}\n7 - {}".format(*patterns))
            direct_pattern = int(input("Select one of above: "))
            if(direct_pattern == 1):
                ingredient1 = int(input("Type first ingredient: "))
                ingredient2 = int(input("Type second ingredient: "))
                sum = ingredient1 + ingredient2
                print("Sum of those numbers is:",sum)
            elif(direct_pattern == 2):
                minuend = int(input("Type minuend: "))
                subtrahend = int(input("Type subtrahend"))
                difference = minuend - subtrahend
                print("Difference of those numbers is:",difference)
            elif(direct_pattern == 3):
                factor1 = int(input("Type first factor: "))
                factor2 = int(input("Type second factor: "))
                product = factor1 * factor2
                print("Product of those numbers is:",product)
            elif(direct_pattern == 4):
                dividend = int(input("Type dividend: "))
                divisor = int(input("Type divisor: "))
                quotient = round(dividend / divisor,4)
                remainder = dividend % divisor
                fullquotient = dividend // divisor
                if(remainder != 0):
                    print(f"Quotient of those numbers is: {quotient} ({fullquotient} and {remainder} remainder)")
                else:
                    print(f"Quotient of those numbers is: {quotient}")
        elif(category == 2):
            patterns = ["Square Diagonal","Square Area","Square Circumference","Rectangle Area","Rectangle Circumference","Triangle Area","Triangle Circumference","Rhombus Area","Rhombus Circumference","Parallelogram Area","Parallelogram Circumference","Trapeze Area","Trapeze Circumference","Circle Area","Circle Circumference","Cube Area","Cube Volume","Cuboid Area","Cuboid Volume","Cylinder Area","Cylinder Volume","Sphere Area","Sphere Volume"]
            print("\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n 7 - {}\n 8 - {}\n 9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}\n22 - {}\n23 - {}\n".format(*patterns))
            direct_pattern = int(input("Select one of above: "))
            if(direct_pattern == 1):
                side_length = int(input("Type side length of your square: "))
                Diagonal = round(side_length * math.sqrt(2),3)
                print("Diagonal of your square is: {}√2 ({})".format(side_length, Diagonal))
            elif(direct_pattern == 2):
                side_length = int(input("Type side lenght of your square: "))
                SquareArea = side_length ** 2
                print("Area of your square is: {}".format(SquareArea))
            elif(direct_pattern == 3):
                side_length = int(input("Type side length of your square: "))
                SquareCirc = side_length * 4
                print("Circumference of your square is: {}".format(SquareCirc))
            elif(direct_pattern == 4):
                RectWidth = int(input("Type width of your rectangle: "))
                Rectheight = int(input("Type height of your rectangle: "))
                RectArea = Rectheight * RectWidth
                print("Area of your rectangle is: {}".format(RectArea))
            elif(direct_pattern == 5):
                RectWidth = int(input("Type width of your rectangle: "))
                Rectheight = int(input("Type height of your rectangle: "))
                RectCirc = 2 * RectWidth + 2 * Rectheight
                print("Circumference of your rectangle is: {}".format(RectCirc))
            elif(direct_pattern == 6):
                side_length = int(input("Type side length of your triangle: "))
                height = int(input("Type height of your triangle: "))
                TriArea = side_length * height / 2
                print("Area of your triangle is {}".format(TriArea))
            elif(direct_pattern == 7):
                triangle_calc()
            elif(direct_pattern == 8):
                rhombus_calc()
            elif(direct_pattern == 9):
                side_length = int(input("Type side length of your rhombus: "))
                RhoCirc = side_length * 4
                print("Circumference of your rhombus is {}".format(RhoCirc))
            elif(direct_pattern == 10):
                side_length = int(input("Type side length of your parallelogram: "))
                height = int(input("Type height of your parallelogram: "))
                ParArea = side_length * height
                print("Area of your parallelogram is {}".format(ParArea))
            elif(direct_pattern == 11):
                side_length1 = int(input("Type first side length of your parallelogram: "))
                side_length2 = int(input("Type second side length of your parallelogram: "))
                ParCirc = (side_length1 + side_length2) * 2
                print("Circumference of your parallelogram is {}".format(ParCirc))
            elif(direct_pattern == 12):
                BaseLength1 = int(input("Type first base length of your trapeze: "))
                BaseLength2 = int(input("Type second base length of your trapeze: "))
                height = int(input("Type height of your trapeze: "))
                TrapArea = (BaseLength1 + BaseLength2) * height / 2
            elif(direct_pattern == 13):
                TrapezeCalc()
            elif(direct_pattern == 14):
                Radius = int(input("Type radius of your circle (half of a diameter): "))
                CirlArea = round(Radius**2 * math.pi, 4)
                print("Area of your circle is: {}π ({})".format(Radius**2,CirlArea))
            elif(direct_pattern == 15):
                Radius = int(input("Type radius of your circle (half of a diameter): "))
                CirlCirc = round(Radius * math.pi * 2, 4)
                print("Circumference of your circle is: {}π ({})".format(Radius * 2,CirlCirc))
            elif(direct_pattern == 16):
                EdgeLength = int(input("Type edge length of your cube: "))
                CubeArea = EdgeLength**2 * 6
                print("Area of your cube is: {}".format(CubeArea))
            elif(direct_pattern == 17):
                EdgeLength = int(input("Type edge length of your cube: "))
                CubeVol = EdgeLength**3
                print("Volume of your cube is: {}".format(CubeVol))
            elif(direct_pattern == 18):
                EdgeLength1 = int(input("Type first edge length of your cube: "))
                EdgeLength2 = int(input("Type second edge length of your cube: "))
                EdgeLength3 = int(input("Type third edge length of your cube: "))
                CuboidArea = (EdgeLength1 * EdgeLength2 + EdgeLength1 * EdgeLength3 + EdgeLength2 * EdgeLength3) * 2
                print("Area of your cuboid is: {}".format(CuboidArea))
            elif(direct_pattern == 19):
                EdgeLength1 = int(input("Type first edge length of your cube: "))
                EdgeLength2 = int(input("Type second edge length of your cube: "))
                EdgeLength3 = int(input("Type third edge length of your cube: "))
                CuboidVol = EdgeLength1 * EdgeLength2 * EdgeLength3
                print("Volume of your cuboid is: {}".format(CuboidVol))
            elif(direct_pattern == 20):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                height = int(input("Type height of your cyliner: "))
                CylArea = math.pi * Radius * (Radius + height) * 2
                print("Area of your cylinder is: {}π ({})".format(Radius*(Radius+height)*2,round(CylArea)))
            elif(direct_pattern == 21):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                height = int(input("Type height of your cyliner: "))
                CylVol = math.pi * Radius**2 * height
                print("Volume of your cylinder is: {}π ({})".format(Radius**2*height,round(CylVol,4)))
            elif(direct_pattern == 22):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                SphArea = math.pi * Radius**2 * 4
                print("Area of your sphere is: {}π ({})".format(Radius**2*4,round(SphArea,4)))
            elif(direct_pattern == 23):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                SphVol = math.pi * Radius**3 * 4 / 3
                print("Volume of your sphere is: {}π ({})".format(Radius**3*4/3,round(SphVol,4)))
            else:
                print("This isn't currently available, but may be in future...")
                Calc()
    elif(branchOfScience == 2):
        patterns = ["Density","Volume","Mass"]
        direct_pattern = int(input("Select one of those: \n1 - {}\n2 - {}\n3 - {}\n".format(*patterns)))
    elif(branchOfScience == 3):
        patterns = ["Byte Calculator"]
        direct_pattern = int(input("Select one of those: \n1 - {}\n".format(*patterns)))
    else:
       print("Type correct number")
       Calc()
Calc()