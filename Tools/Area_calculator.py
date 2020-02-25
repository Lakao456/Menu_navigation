k = 0
print("Select a number accordingly")
print("1--Calculate area of a Square",
      "2--Calculate area of a Circle",
      "3--Calculate area of a Rectangle",
      "4--Calculate area of a Cylinder",
      "5--Calculate area of a Sphere",
      "----------OR----------",
      "Enter exit to end the program",
      sep='\n', end="\n ----------------------------- \n")
while (k == 0):
    n = input("Enter the number::")
    if "e" in n.lower():
        k = 1
    elif int(n) == 1:
        s = float(input("Enter the side of the square::"))
        print("The area of the square is", s ** 2)
    elif int(n) == 2:
        r = float(input("Enter the radius of the circle::"))
        print("The area of the circle is", 3.14 * (r ** 2))
    elif int(n) == 3:
        l = float(input("Enter the length of the rectangle::"))
        w = float(input("Enter the width of the rectangle::"))
        print("The area of the rectangle is", l * w)
    elif int(n) == 4:
        r = float(input("Enter the radius of the base::"))
        h = float(input("Enter the hieght of the cylinder::"))
        print("The area of the cylinder is", 2 * 3.14 * r * (r + h))
    elif int(n) == 5:
        r = float(input("Enter the radius of the sphere::"))
        print("The area of the sphere is", (3 / 4) * 3.14 * (r ** 3))
print("Thank you")
