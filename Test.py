# Example 4

import math

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area(radius)
    print(f"area: {area:.1f}")

def circle_area(radius):
    area = math.pi * radius * radius
    return area

main()