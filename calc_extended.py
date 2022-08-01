#Ask for question Category
import sys
Category = int(input("Enter category of your question: \nType 1 for Maths\nType 2 for Chemistry\nType 3 for Informatics\n:"))
if(Category == 1):
    Patterns = ["SquareDiagonal","SquareArea","SquareCircuit","RectangleArea","RectangleCircuit","TriangleArea","TriangleCircuit","RhombusArea","RhombusCircuit","ParallelogramArea","ParallelogramCircuit","TrapezeArea","TrapezeCircuit","SphereArea","SphereCircuit","CubeArea","CubeVolume","CuboidArea","CuboidVolume","CylinderArea","CylinderVolume"]
elif(Category == 2):
    Patterns = ["Density","Volume","Mass"]
elif(Category == 3):
    Patterns = ["ByteCalculator"]
else:
    print("Type correct number")
print("Select one of those: \n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n 6 - {}\n 7 - {}\n 8 - {}\n 9 - {}\n10 - {}\n11 - {}\n12 - {}\n13 - {}\n14 - {}\n15 - {}\n16 - {}\n17 - {}\n18 - {}\n19 - {}\n20 - {}\n21 - {}".format(Patterns[0],Patterns[1],Patterns[2],Patterns[3],Patterns[4],Patterns[5],Patterns[6],Patterns[7],Patterns[8],Patterns[9],Patterns[10],Patterns[11],Patterns[12],Patterns[13],Patterns[14],Patterns[15],Patterns[16],Patterns[17],Patterns[18],Patterns[19],Patterns[20]))
