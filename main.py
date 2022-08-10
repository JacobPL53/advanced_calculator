import math
# Creating global variables: 'DirectPattern' - String and 'Patterns' - Array
direct_pattern = ""
patterns = []
def triangle_calc():
    triangle = str(input("Is your triangle equilateral or isosceles or different-sided?(e/i/d): "))
    if(triangle == "e" or triangle == "E"):
        SideLength = int(input("Type side length of your triangle: "))
        TriCirc = SideLength * 3
        print("Circumference of your triangle is: {}".format(TriCirc))
    elif(p == "i" or triangle == "I"):
        TriLeg = int(input("Type legs length in your triangle: "))
        TriBase = int(input("Type base length in your triangle: "))
        TriCirc = TriLeg * 2 + TriBase
        print("Circumference of your triangle is: {}".format(TriCirc))
    elif(triangle == "d" or triangle == "D"):
        TriSide1 = int(input("Type first side length in your triangle: "))
        TriSide2 = int(input("Type secord side length in your triangle: "))
        TriSide3 = int(input("Type third side length in your triangle: "))
        TriCirc = TriSide1 + TriSide2 + TriSide3
        print("Circumference of your triangle is: {}".format(TriCirc))
    else:
        print("Type correct letter: e or i or d")
        trianglecalc()
def RhombusCalc():
    DiagOrSide = input("Formula with diagonals or with a side?(d/s)")
    if(DiagOrSide == "d" or DiagOrSide == "D"):
        RhoDiag1 = int(input("Type first diagonal of your rhombus: "))
        RhoDiag2 = int(input("Type second diagonal of your rhombus: "))
        RhoArea = RhoDiag1 * RhoDiag2 / 2
        print("Area of your rhombus is: {}".format(RhoArea))
    elif(DiagOrSide == "s" or DiagOrSide == "S"):
        SideLength = int(input("Type side length of your rhombus: "))
        Height = int(input("Type height of your rhombus: "))
        RhoArea = SideLength * Height
        print("Area of your rhombus is: {}".format(RhoArea))
    else:
        print("Type correct letter: d or s")
        RhombusCalc()
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
        Categories = ["Basic Calculator","Geometry"]
        Category = int(input("1 - {}\n2 - {}\nSelect one of those: ".format(*Categories)))
        if(Category == 1):
            Patterns = ["Addition","Substraction","Multiplication","Division","Power","Root","Modulo"]
            print("Basic Calculator isn't available now.")
            Calc()
        elif(Category == 2):
            Patterns = ["Square Diagonal","Square Area","Square Circumference","Rectangle Area","Rectangle Circumference","Triangle Area","Triangle Circumference","Rhombus Area","Rhombus Circumference","Parallelogram Area","Parallelogram Circumference","Trapeze Area","Trapeze Circumference","Circle Area","Circle Circumference","Cube Area","Cube Volume","Cuboid Area","Cuboid Volume","Cylinder Area","Cylinder Volume","Sphere Area","Sphere Volume"]
            print("\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n 7 - {}\n 8 - {}\n 9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}\n22 - {}\n23 - {}\n".format(*Patterns))
            DirectPattern = int(input("Select one of above: "))
            if(DirectPattern == 1):
                SideLength = int(input("Type side length of your square: "))
                Diagonal = round(SideLength * math.sqrt(2),3)
                print("Diagonal of your square is: {}√2 ({})".format(SideLength, Diagonal))
            elif(DirectPattern == 2):
                SideLength = int(input("Type side lenght of your square: "))
                SquareArea = SideLength ** 2
                print("Area of your square is: {}".format(SquareArea))
            elif(DirectPattern == 3):
                SideLength = int(input("Type side length of your square: "))
                SquareCirc = SideLength * 4
                print("Circumference of your square is: {}".format(SquareCirc))
            elif(DirectPattern == 4):
                RectWidth = int(input("Type width of your rectangle: "))
                RectHeight = int(input("Type height of your rectangle: "))
                RectArea = RectHeight * RectWidth
                print("Area of your rectangle is: {}".format(RectArea))
            elif(DirectPattern == 5):
                RectWidth = int(input("Type width of your rectangle: "))
                RectHeight = int(input("Type height of your rectangle: "))
                RectCirc = 2 * RectWidth + 2 * RectHeight
                print("Circumference of your rectangle is: {}".format(RectCirc))
            elif(DirectPattern == 6):
                SideLength = int(input("Type side length of your triangle: "))
                Height = int(input("Type height of your triangle: "))
                TriArea = SideLength * Height / 2
                print("Area of your triangle is {}".format(TriArea))
            elif(DirectPattern == 7):
                trianglecalc()
            elif(DirectPattern == 8):
                RhombusCalc()
            elif(DirectPattern == 9):
                SideLength = int(input("Type side length of your rhombus: "))
                RhoCirc = SideLength * 4
                print("Circumference of your rhombus is {}".format(RhoCirc))
            elif(DirectPattern == 10):
                SideLength = int(input("Type side length of your parallelogram: "))
                Height = int(input("Type height of your parallelogram: "))
                ParArea = SideLength * Height
                print("Area of your parallelogram is {}".format(ParArea))
            elif(DirectPattern == 11):
                SideLength1 = int(input("Type first side length of your parallelogram: "))
                SideLength2 = int(input("Type second side length of your parallelogram: "))
                ParCirc = (SideLength1 + SideLength2) * 2
                print("Circumference of your parallelogram is {}".format(ParCirc))
            elif(DirectPattern == 12):
                BaseLength1 = int(input("Type first base length of your trapeze: "))
                BaseLength2 = int(input("Type second base length of your trapeze: "))
                Height = int(input("Type height of your trapeze: "))
                TrapArea = (BaseLength1 + BaseLength2) * Height / 2
            elif(DirectPattern == 13):
                TrapezeCalc()
            elif(DirectPattern == 14):
                Radius = int(input("Type radius of your circle (half of a diameter): "))
                CirlArea = round(Radius**2 * math.pi, 4)
                print("Area of your circle is: {}π ({})".format(Radius**2,CirlArea))
            elif(DirectPattern == 15):
                Radius = int(input("Type radius of your circle (half of a diameter): "))
                CirlCirc = round(Radius * math.pi * 2, 4)
                print("Circumference of your circle is: {}π ({})".format(Radius * 2,CirlCirc))
            elif(DirectPattern == 16):
                EdgeLength = int(input("Type edge length of your cube: "))
                CubeArea = EdgeLength**2 * 6
                print("Area of your cube is: {}".format(CubeArea))
            elif(DirectPattern == 17):
                EdgeLength = int(input("Type edge length of your cube: "))
                CubeVol = EdgeLength**3
                print("Volume of your cube is: {}".format(CubeVol))
            elif(DirectPattern == 18):
                EdgeLength1 = int(input("Type first edge length of your cube: "))
                EdgeLength2 = int(input("Type second edge length of your cube: "))
                EdgeLength3 = int(input("Type third edge length of your cube: "))
                CuboidArea = (EdgeLength1 * EdgeLength2 + EdgeLength1 * EdgeLength3 + EdgeLength2 * EdgeLength3) * 2
                print("Area of your cuboid is: {}".format(CuboidArea))
            elif(DirectPattern == 19):
                EdgeLength1 = int(input("Type first edge length of your cube: "))
                EdgeLength2 = int(input("Type second edge length of your cube: "))
                EdgeLength3 = int(input("Type third edge length of your cube: "))
                CuboidVol = EdgeLength1 * EdgeLength2 * EdgeLength3
                print("Volume of your cuboid is: {}".format(CuboidVol))
            elif(DirectPattern == 20):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                height = int(input("Type height of your cyliner: "))
                CylArea = math.pi * Radius * (Radius + height) * 2
                print("Area of your cylinder is: {}π ({})".format(Radius*(Radius+height)*2,round(CylArea)))
            elif(DirectPattern == 21):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                height = int(input("Type height of your cyliner: "))
                CylVol = math.pi * Radius**2 * height
                print("Volume of your cylinder is: {}π ({})".format(Radius**2*height,round(CylVol,4)))
            elif(DirectPattern == 22):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                SphArea = math.pi * Radius**2 * 4
                print("Area of your sphere is: {}π ({})".format(Radius**2*4,round(SphArea,4)))
            elif(DirectPattern == 23):
                Radius = int(input("Type radius of your cylinder (half of a diameter): "))
                SphVol = math.pi * Radius**3 * 4 / 3
                print("Volume of your sphere is: {}π ({})".format(Radius**3*4/3,round(SphVol,4)))
            else:
                print("This isn't currently available, but may be in future...")
                Calc()
    elif(branchOfScience == 2):
        Patterns = ["Density","Volume","Mass"]
        DirectPattern = int(input("Select one of those: \n1 - {}\n2 - {}\n3 - {}\n".format(*Patterns)))
    elif(branchOfScience == 3):
        Patterns = ["Byte Calculator"]
        DirectPattern = int(input("Select one of those: \n1 - {}\n".format(*Patterns)))
    else:
       print("Type correct number")
       Calc()
Calc()