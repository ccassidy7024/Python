#Python program showcasing use of classes with private variables and calling instances
#Defines Person class
class Person:
    #initializes private variables of name, address, age, and phone number
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    #defines getter methods for each piece of data allowing user to access data
    def get_info(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone_number
    #defines setter methods for each piece of data allowing user to change data
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
#creates instances using Person class with specific variable information
person1 = Person("Devin", "55 Avenue St.", "31", "5556903348")
person2 = Person("Kayla", "434 Oak Blvd", "28", "5556789034")
person3 = Person("Chuck", "77 Eerie Way", 19, "5553709276")
#prints organized format listing each piece of data as input
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())