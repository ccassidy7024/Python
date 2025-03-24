#Python program that calculates the factorial of a number using recursive functions

#Defines recursive function to calculate the factorial of a number if the number is 1 or greater
def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n-1)
#Defines main function to call factorial function to print      
def main():
    n = int(input("Enter a non-negative number: "))
    result = factorial(n)
    print(factorial(n))
#Calls function with calculated factorial
main()