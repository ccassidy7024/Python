#Python program demonstrating creating objects with properties defined within a class with a Veterinary Office Pet System
#Defines pet class
class Pet:
    #Sets default variable
    pet_type = "Dog"
    def __init__(self, name, owner_name, size, color, breed, age, vet_name="Smiley's Veterinary Hospital"):
        #Set instance variables
        self.name = name
        self.owner_name = owner_name
        self.size = size
        self.color = color
        self.breed = breed
        self.age = age
        self.vet_name = vet_name

    #Getters and Setters for each instance variable
    def get_name(self):
        return self.name
    def get_owner_name(self):
        return self.owner_name
    def get_size(self):
        return self.size
    def get_color(self):
        return self.color
    def get_breed(self):
        return self.breed
    def get_age(self):
        return self.age
    def set_name(self, value):
        self.name = value
    def set_owner_name(self, value):
        self.owner_name = value
    def set_size(self, value):
        self.size = value
    def set_color(self, value):
        self.color = value
    def set_breed(self, value):
        self.breed = value
    def set_age(self, value):
        self.age = value
    def set_vet_name(self, value):
        self.vet_name = value
#Method to print details of the pet and its owner
    def display_pet_info(self):
       print("Pet and Owner details: ")
       print("Pet's name: ", self.name)
       print("Owner's name: ", self.owner_name)
       print("Pet's size: ", self.size)
       print("Pet's color: ", self.color)
       print("Pet's breed: ", self.breed)
       print("Pet's age: ", self.age)
       print("Primary Veterinary Care Facility: ", self.vet_name)
#Defines main function to use Pet class
def main():
#Instantiates three pet objects with different details
    petpatient_beanie = Pet("Beanie", "Sean Holder", "Medium", "Chocolate", "Labrador", "4")

    petpatient_waffles = Pet("Waffles", "Amber Banks", "Large", "Grey", "Pitbull", "7")

    petpatient_snowball = Pet("Snowball", "Brittney Lopper", "Small", "White", "Chihuahua", "10")

    print(petpatient_beanie.get_name())
    petpatient_beanie.display_pet_info()
    print("\n")
    print(petpatient_waffles.get_name())
    petpatient_waffles.set_age("9")
    petpatient_waffles.display_pet_info()
    print("\n")
    print(petpatient_snowball.get_name())
    petpatient_snowball.display_pet_info()

def check_property():
        print("Are there further records available?")
        value = input("Enter an information field to search: ")
        if value != main:
            try:
                hasattr(Pet.value)
            except AttributeError:
                print("False. Attribute variable does not exist")
            else:
                print("True")
main()
print("\n")
check_property()