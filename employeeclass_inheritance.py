#Python program that defines an Employee class and creates subclasses with additional attributes that inherit from Employee
#Defines Employee class
class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number
    
#Defines ProductionWorker subclass with extra attributes
class ProductionWorker(Employee):
    def __init__(self, employee_name="", employee_number="", shift_number=(1,2), hourly_pay=0.0):
        super().__init__(employee_name, employee_number)
        self.shift_number = shift_number
        self.hourly_pay = hourly_pay
    #Defines getter and setter methods for each attribute included additional ones found in subclass
    def set_employee_name(self, value):
        self.employee_name = value
    def get_employee_name(self):
        return self.employee_name
    def set_employee_number(self, value):
        self.employee_number = value
    def get_employee_number(self):
        return self.employee_number
    def get_shift_number(self):
        return self.shift_number
    #try except block used to ensure user can only enter "1" or "2" for day or night shift and no other numbers
    def set_shift_number(self, value):
        try: 
            if self.shift_number >0 and self.shift_number <=2:
                self.shift_number = value
        except ValueError:
            print("Shift number must be 1 or 2 - 1 for day shift or 2 for night shift")
    def set_hourly_pay(self, value):
        self.hourly_pay = value
    def get_hourly_pay(self):
        return self.hourly_pay
        
    #Defines __str__ method to print user-friendly output of entered Employee information
    def __str__(self):
        return f"Employee: Name: {self.employee_name}\n Employee Number: {self.employee_number}\n Shift Number: {self.shift_number}\n Hourly Pay Rate: ${self.hourly_pay}"


#Creates an instance of ProductionWorker
def main():
    print("Please enter the following details about the Employee: ")
    print("\n\n")
    #Takes user input for attribute values
    employee_name = input("Enter Employee's Name: ")
    employee_number = input("Enter Employee Number: ")
    employee_shift = int(input("Enter Shift Number: "))
    employee_hourly = float(input("Enter Hourly Pay: $"))
    employee = ProductionWorker(employee_name, employee_number, employee_shift, employee_hourly)
    print("\n\n")
    print(f"New Employee Information: ")
    #Prints employee information using details input by user
    print(employee.__str__())
    
#Calls main function
main()
   
        