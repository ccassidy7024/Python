#Python program that creates a custom exception class to handle specific error scenarios
#Defines custom  error class
class InvalidInputErrorr(Exception):
        def __init__(self, error="Invalid Input Error. Please enter valid number"):
             self.error

#Defines custom exception class
class NotNumericError(Exception):
    def __init__(self, message="Please enter a valid number"):

        self.message = message
        super().__init__(self,message)

        try:
                raise InvalidInputErrorr("Invalid input")
        except InvalidInputErrorr as e:
                print("Invalid input. Please enter an integer or valid number")
        else:
            print("Valid Input")
        finally:
            print("No errors occurred")