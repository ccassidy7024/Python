import math

def rectangle_area(length, width):
    return length * width
def square_area(length):
    return length ** 2
def circle_area(radius):
    return math.pi * radius ** 2
def polygon_area(length, apothem):
    perimeter = sum(length)
    return 0.5 * perimeter * apothem

length = 12
width = 14
calculate_rectangle = rectangle_area(length, width)
print("\nThe area of this rectangle is", {calculate_rectangle})

length = 4
calculate_square = square_area(length)
print("\nThe area of this square is", {calculate_square})

radius = 7
calculate_circle = circle_area(radius)
print("\nThe area of this circle is", {calculate_circle})

polygon_sides = [3, 3, 3, 3, 3, 3]
apothem_polygon = 4.33
calculate_polygon = polygon_area(polygon_sides, apothem_polygon)
print("\nThe area of this polygon is", {calculate_polygon})