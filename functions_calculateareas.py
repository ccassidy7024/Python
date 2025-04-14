# Python program that calculates areas using two functions -
# one calculates the area of a square and the other calculates the area of a circle

# Function to calculate area of a square
def square_function(side):
    print("The area of the square is", side * side, "square units")


# Calls the square function with sample value
square_function(3)

# Function to calculate area of a circle


def circle_function(radius):
    print("The area of the circle is", (3.14)*radius*radius,
          "square units")  # multiplies radius by value of pi


# Calls the circle function with sample value
circle_function(7)
