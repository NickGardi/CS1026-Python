#Nicholas Gardi     Assignment 2

#import math to use the exact value of pi
import math

#defining the function for volume of a cube
def cubeVolume(sideLength):
    sideLength = float(input("Enter the side length of the cube: "))
    volume = sideLength ** 3
    return volume

#defining the function for volume of a pyramid
def pyramidVolume(baseLength, heightLength):
    baseLength = float(input("Enter the base length of the pyramid: "))
    heightLength = float(input("Enter the height length of the pyramid: "))
    volume = (1/3)*(baseLength ** 2)*(heightLength)
    return volume

#defining the function for volume of a ellipsoid
def ellipsoidVolume(rediusLength):
    radiusLength = float(input("Enter the length of the radius of the ellipsoid: "))
    volume = (3/4)*(math.pi)*(radiusLength ** 3)
    return volume

#defining the lists to contain the final volumes
cubeList = []
pyramidList = []
ellipsoidList = []

#while loop to continue asking for inputs until the user types in quit
i = 1
while i > 0:
    shape = input("Enter the shape(Cube, Pyramid, Ellipsoid) for which you would like to calculate the volume of, or type 'quit' to end the program: ").lower()
    #validating the user input
    if shape not in ("cube", "pyramid", "ellipsoid", "quit"):
        print("Please enter one of the folowing choices below: cube, pyramid, ellipsoid, or quit.")
    #calling the cube volume function and added the answer to the list
    if shape == "cube":
        sideLength = 0
        cubeList.append(cubeVolume(sideLength))
    #calling the pyramid volume function and added the answer to the list
    if shape == "pyramid":
        baseLength = 0
        heightLength = 0
        pyramidList.append(pyramidVolume(baseLength, heightLength))
    #calling the ellipsoid volume function and added the answer to the list
    if shape == "ellipsoid":
        radiusLength = 0
        ellipsoidList.append(ellipsoidVolume(radiusLength))
    if shape == "quit":
    #stopping the while loop and printing out the required strings/volumes
        if cubeList == [] and pyramidList == [] and ellipsoidList == []:
            i = -1
            print("You have come to the end of the session.")
            print("You did not perform any volume calculations")
        else:
            #sorting the lists
            cubeList.sort()
            pyramidList.sort()
            ellipsoidList.sort()
            i = -1
            print("You have come to the end of the session.")
            print("The volumes calculated for each shape are shown below")
            print("Cube: " + str(cubeList)[1:-1])
            print("Pyramid: " + str(pyramidList)[1:-1])
            print("Ellipsoid: " + str(ellipsoidList)[1:-1])
