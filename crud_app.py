#Python program that develops basic CRUD application
#Main menu function display a main menu to the user

#Provided function to display main menu with CRUD options to user
def main_menu():
        print("Menu:")
        while True:
            try:
                print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
                print("1. Create a new entry")
                print("2. Display an entry by last name")
                print("3. Update an existing entry")
                print("4. Remove an entry")
                print("5. Quit")
                choice = int(input("Please enter the number of your selection: "))
                if 1 <= choice <= 5:        #ensures users choose numbers associated with CRUD operation options provided
                    return choice
                else:
                    print("That is not a valid number. Try again.")
            except ValueError:
                print("That is not a valid number. Try again.")   #try except block handles error in case number less than 1 or greater than 5 is entered
#Defines check function which references text file with data and uses readlines() to iterate through all customer entries
def check():
        try:
            file = open("customer_list.txt", 'r')       #opens text file in read mode
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError:                   #exceptions if incorrect file is entered
            print("Customer list does not exist. Creating a new file...")
        except TypeError:
            print("Invalid input")
            return []
#Defines create function which adds new entries to customer list on text file.
def create():
        customer = check()
        fname = input("Please enter the customer\'s first name: ")
        lname = input("Please enter the customer\'s last name: ")
        phone = input("Please enter the customer\'s phone: ")
        email = input("Please enter the customer\'s email: ")
        entry = f"{fname}, {lname}, {phone}, {email} \n"
        customer.append(entry)
        save(customer)
#Defines save function which saves newly created entry from create() function to file
def save(output):
        file = open("customer_list.txt", 'w')
        for line in output:
            file.write(line)
        file.close()
        print("File updated.")
#Defines read function which allows user to retrieve and view existing data from file
def read():
        customer = check()      #checks existing file data against user input when searched
        lname_check = input("Please enter the customer\'s last name to search: ").strip().lower()  #strip removes extra space and lower takes any capitalization input for info
        print("Reading an entry...")
        entry_exists = False
        while not entry_exists:
            try: 
                for line in customer:
                    if lname_check in line.lower():
                        print(f'Customer information: {line.strip()}')      #retrieves and prints just the line of customer information matching the last name entered by user
                        entry_exists = True
            except TypeError:
                print("Invalid entry.")             #try except blocks with exceptions to handle wrong name inputs or incorrect inputs
            except ValueError:
                 print("Not a valid string.")
            except NameError:
                print("Customer does not exist in database")
#Defines update which allows user to modify information on existing file data
def update():
        customer = check()
        update_entry = input("Please enter the customer\'s last name to update entry: ").strip().lower()
        try:
            for i, entry in enumerate(customer):        #iterates through each entry with index and values to go in order
                if update_entry.lower() in entry.lower():
                    print(f'Current customer information: ', entry.strip())
                    updated_fname = input("Please enter new first name to update information with: ")       #allows for new input for updated info
                    updated_lname = input("Please enter new last name to update information with: ")
                    updated_phone = input("Please enter new phone number to update information with: ")
                    updated_email = input("Please enter new email to update information with: ")
                    updated_info = f'{updated_fname}, {updated_lname}, {updated_phone}, {updated_email} \n'    
                    customer[i] = updated_info
                    save(customer)      #saves updated information to customer on file with last name entered
                    print("Updating an entry...")
        except TypeError:
                print("Invalid entry.")
        except ValueError:
                 print("Not a valid string.")
        except NameError:
                print("Customer does not exist in database")
#Defines detailed which removes existing entries from file
def delete():
    customer = check()
    delete_entry = input("Please enter the customer\'s last name to delete entry: ").strip().lower()
    new_list = []   #empty list allows for updated list without deleted entry to be saved to file
    try: 
        for entry in customer:
            if delete_entry not in entry.lower():       #loops through file to check for last name entered and appends entry 
                new_list.append(entry)
        if len(new_list) != len(customer):          #len determines number of items in new list and if it does not equal the number of entries on the original list
            save(new_list)                          #the new list is saved to the file 
            print("Deleting an entry...")
            return
        else:
            print("No entry found with that last name.")
    except TypeError:
                print("Invalid entry")
    except ValueError:
                 print("Not a valid string")
    except NameError:
                print("Customer does not exist in database")
#Provided main() function
def main():
    choice = 0
    while choice != 5:              #while loop cycles through 1-5 based on choice from main_menu function and returns associated CRUD function
        choice = main_menu()        #calls main_menu function to associate user input choice with number and CRUD operation associations
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
    print("\nData saved as customer_list.txt\n")
#Calls main function
main()
