import math
#Creating global variables: 'DirectPattern' - String and 'Patterns' - Array
DirectPattern = ""
Patterns = []
#Ask for question branch
def TriangleCalc():
    Triangle = str(input("Is your triangle equilateral or isosceles or different-sided?(e/i/d): "))
    if(Triangle == "e" or Triangle == "E"):
        SideLength = int(input("Type side length of your triangle: "))
        TriCirc = SideLength * 3
        print("Circuit of your triangle is: {}".format(TriCirc))
    elif(Triangle == "i" or Triangle == "I"):
        TriLeg = int(input("Type legs length in your triangle: "))
        TriBase = int(input("Type base length in your triangle: "))
        TriCirc = TriLeg * 2 + TriBase
        print("Circuit of your triangle is: {}".format(TriCirc))
    elif(Triangle == "d" or Triangle == "D"):
        TriSide1 = int(input("Type first side length in your triangle: "))
        TriSide2 = int(input("Type secord side length in your triangle: "))
        TriSide3 = int(input("Type third side length in your triangle: "))
        TriCirc = TriSide1 + TriSide2 + TriSide3
        print("Circuit of your triangle is: {}".format(TriCirc))
    else:
        print("Type correct letter: e or i or d")
        TriangleCalc()
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
def Calc():
    branchOfScience = int(input("Enter branch of your question: \nType 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics\n:"))
    if(branchOfScience == 1):
        Categories = ["Basic Calculator","Geometry"]
        Category = int(input("1 - {}\n2 - {}\nSelect one of those: ".format(*Categories)))
        if(Category == 1):
            Patterns = ["Addition","Substraction","Multiplication","Division","Power","Root","Modulo"]
            print("Basic Calculator isn't available now.")
            Calc()
        elif(Category == 2):
            Patterns = ["Square Diagonal","Square Area","Square Circuit","Rectangle Area","Rectangle Circuit","Triangle Area","Triangle Circuit","Rhombus Area","Rhombus Circuit","Parallelogram Area","Parallelogram Circuit","Trapeze Area","Trapeze Circuit","Sphere Area","Sphere Circuit","Cube Area","Cube Volume","Cuboid Area","Cuboid Volume","Cylinder Area","Cylinder Volume"]
            print("\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n 7 - {}\n 8 - {}\n 9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}\n".format(*Patterns))
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
                print("Circuit of your square is: {}".format(SquareCirc))
            elif(DirectPattern == 4):
                RectWidth = int(input("Type width of your rectangle: "))
                RectHeight = int(input("Type height of your rectangle: "))
                RectArea = RectHeight * RectWidth
                print("Area of your rectangle is: {}".format(RectArea))
            elif(DirectPattern == 5):
                RectWidth = int(input("Type width of your rectangle: "))
                RectHeight = int(input("Type height of your rectangle: "))
                RectCirc = 2 * RectWidth + 2 * RectHeight
                print("Circuit of your rectangle is: {}".format(RectCirc))
            elif(DirectPattern == 6):
                SideLength = int(input("Type side length of your triangle: "))
                Height = int(input("Type height of your triangle: "))
                TriArea = SideLength * Height / 2
                print("Area of your triangle is {}".format(TriArea))
            elif(DirectPattern == 7):
                TriangleCalc()
            elif(DirectPattern == 8):
                RhombusCalc()
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