#Python program that implements a class (Pet) with specific attributes and methods
#Creates Pet Class
class Pet:
    #Sets instance variables
    def __init__(self, kind, breed, name):
        self.kind = kind
        self.breed = breed
        self.name = name
    #Sets getter and setter methods for each attribute
    def get_kind(self):
        return self.kind
    def get_breed(self):
        return self.breed
    def get_name(self):
        return self.name
    def set_kind(self, value):
        self.kind = value
    def set_breed(self, value):
        self.breed = value
    def set_name(self, value):
        self.name = value
#Method to print details of the pet
    def print_details(self):
            print("Pet Details: ", vars(self))
#Defines main function to use instances of Pet class
def main():
    #Creates three objects of Pet class with different kinds, breeds, and names
    petclass_dog = Pet("Dog", "Terrier", "Winston")
    print(petclass_dog.get_kind())
    #Calls the print_details method to print details of each object created
    petclass_dog.print_details()
    petclass_cat = Pet("Cat", "Tabby", "Persephone")
    print(petclass_cat.get_kind())
    petclass_cat.print_details()
    petclass_bunny = Pet("Bunny", "Holland Lop", "Cooper")
    print(petclass_bunny.get_kind())
    petclass_bunny.print_details()

    #Uses the __name__ method with Pet class
    print(f"Name of the Class: {Pet.__name__}")
    #Uses  getattr() method to get an attribute from instance of bunny object of Pet class
    print(f"Access the breed attribute of the 'Bunny' object: {getattr(petclass_bunny, 'breed')}")
    #Uses isinstance() method to return True or False boolean if cat is an instance of Pet class
    print(f"Is 'Cat' and instance of the Pet class?: {isinstance(petclass_cat, Pet)}")
    #try and except block to handle possible errors when setting new information for instance attributes
    try:
        user_set = input()
        value = Pet.set_name(user_set)
    except ValueError:
        print("Invalid input. Please check spelling and try again")
    except SyntaxError:
        print("Invalid input. Please check spelling and try again")
#Calls main function
main()

