import math
#Creating global variables: 'DirectPattern' - String and 'Patterns' - Array
DirectPattern = ""
Patterns = []
#Ask for question Category
Category = int(input("Enter category of your question: \nType 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics\n:"))
if(Category == 1):
    Patterns = ["Square Diagonal" """Square Side from Area","Square Side from Square Circuit""","Square Area","Square Circuit","Rectangle Area","Rectangle Circuit","Triangle Area","Triangle Circuit","Rhombus Area","Rhombus Circuit","Parallelogram Area","Parallelogram Circuit","Trapeze Area","Trapeze Circuit","Sphere Area","Sphere Circuit","Cube Area","Cube Volume","Cuboid Area","Cuboid Volume","Cylinder Area","Cylinder Volume"]
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
        SquareCircuit = SideLength * 4
        print("Circuit of your square is: {}".format(SquareCircuit))
    elif(DirectPattern == 4):
        RectWidth = int(input("Type width of your rectangle: "))
        RectHeight = int(input("Type height of your rectangle: "))
        RectArea = RectHeight * RectWidth
        print("Area of your rectangle is: {}".format(RectArea))
    else:
        print("This isn't currently available, but may be in future...")
elif(Category == 2):
    Patterns = ["Density","Volume","Mass"]
    DirectPattern = int(input("Select one of those: \n1 - {}\n2 - {}\n3 - {}\n".format(*Patterns)))
elif(Category == 3):
    Patterns = ["Byte Calculator"]
    DirectPattern = int(input("Select one of those: \n1 - {}\n".format(*Patterns)))
else:
    print("Type correct number")
