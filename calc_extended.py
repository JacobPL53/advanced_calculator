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
print("Select one of those: {0}".format(Patterns))
