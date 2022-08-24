import math

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area()
    print(f"area: {area:.1f}")

def circle_area():
    # Mistake! There is no variable named radius
    # defined inside this function, so the variable
    # radius cannot be used in this function.
    area = math.pi * radius * radius
    return area

main()